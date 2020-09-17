# RadioFlowGraph.py
# Handles gnuradio flowgraph blocks and connections


from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
import osmosdr


class RadioFlowGraph(gr.top_block):
    def __init__(self, radio_id, frequency, freq_offset=0, data_port=8888):
        gr.top_block.__init__(self)

        self.radio_id = radio_id # radio id string (osmosdr radio id)
        self.data_port = int(data_port) # network port used to communicate data back to caller (rx only)
        self.frequency = frequency
        self.freq_offset = freq_offset
        # max radio sample rate is 20Ms/sec, minimum is 2Ms/sec, due to HackRF frontend noise 
        # the ideal minimum is 8Ms/sec
        #self.radio_sample_rate = 8e6
        self.radio_sample_rate = 20e6
        self.bandwidth = 5e3 # set low to ensure we don't leak RF everywhere during transmit
        self.transition = 500 # used by low-pass filters
        self.tx_rf_gain = 0 # dB, 0 or 14 (no steps available)
        self.tx_if_gain = 3 # dB, 0 to 47 in 1 dB steps
        # intermediate sample rates for the rational resamplers, need enough resamplers and
        # sample rates chosen so no single resampler has a decimation greater than 200 due
        # to block/window limitations
        self.int1_sample_rate = 200000 # max radio sample rate = 20Ms/sec, decimate by <= 100
        self.int2_sample_rate = 10000 # int1 sample rate decimated by 10
        self.final_sample_rate = 2000 # final sample rate
        # TODO get sample rates and numbers from outside
        self.num_final_samples = 1000 # recorded samples for each point on the antenna sphere, ideal min 1000
        # calculate the total number of samples so the flowgraph buffers are empty at the
        # right time, stopping further capturing and processing of unneeded samples
        self.num_total_samples = int((float(self.num_final_samples)/self.final_sample_rate)*self.radio_sample_rate)
        self.flowgraph_created = False
        self.is_transmitter = False


    def set_tx_gain(self, tx_rf_gain, tx_if_gain):
        if self.flowgraph_created:
            print("ERROR: Cannot change parameters after flowgraph has been constructed!")
            return False
        # make sure provided gain values are within acceptable range
        # tx_rf_gain is 0 or 14 dB (no steps available)
        # tx_if_gain is 0 to 47 dB in 1 dB steps
        if tx_rf_gain == 0 or tx_rf_gain == 14:
            self.tx_rf_gain = int(tx_rf_gain)
        else:
            print("WARNING: tx_rf_gain can only be 0 or 14, setting to 0.")
            tx_rf_gain = 0
        if tx_if_gain >= 0 or tx_rf_gain <= 47:
            self.tx_if_gain = int(tx_if_gain)
        else:
            print("WARNING: tx_if_gain must be between 0 and 47, setting to 0.")
            tx_if_gain = 0
        return True


    def start(self):
        # we can't reuse the flowgraph without resetting the head block which
        # limits the number of samples captured and processed
        # head block only present on receiver
        if not self.is_transmitter:
            self.blocks_head_0.reset()
        gr.top_block.start(self)


    def setup_flowgraph(self, transmitter=False):
        self.is_transmitter = transmitter
        # create the flowgraph blocks and connections
        if transmitter:
            self._setup_transmitter()
        else:
            self._setup_receiver()
        self.flowgraph_created = True
        return


    def _setup_receiver(self):
        ### receiver blocks ###
        self.osmosdr_source_0 = osmosdr.source(args="numchan=1"+" "+self.radio_id)
        self.osmosdr_source_0.set_sample_rate(self.radio_sample_rate)
        self.osmosdr_source_0.set_center_freq(self.frequency+self.freq_offset, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(int(self.bandwidth*10), 0)

        # something in the resampler blocks is causing 34 output samples to be lost in each
        # resampler, so adjust the total number in order to compensate for these lost samples,
        # calculating backwards up the path so the number gets scaled up by each decimation amount
        num_adjusted_samples = (34+self.num_final_samples)*(self.int2_sample_rate/self.final_sample_rate)
        num_adjusted_samples = (34+num_adjusted_samples)*(self.int1_sample_rate/self.int2_sample_rate)
        num_adjusted_samples = int((34+num_adjusted_samples)*(self.radio_sample_rate/self.int1_sample_rate))

        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, num_adjusted_samples)
        
        self.rational_resampler_recv_0 = filter.rational_resampler_ccc(
            interpolation=1,
            decimation=int(self.radio_sample_rate/self.int1_sample_rate),
            taps=None,
            fractional_bw=None,
            )
        
        #self.low_pass_filter_recv_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        #    1, self.int1_sample_rate, self.bandwidth*2, self.transition, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_recv_0 = filter.fir_filter_ccf(1, firdes.low_pass(
            1, self.int1_sample_rate, self.bandwidth, self.transition, firdes.WIN_HAMMING, 6.76))
        
        self.rational_resampler_recv_1 = filter.rational_resampler_ccc(
            interpolation=1,
            decimation=int(self.int1_sample_rate/self.int2_sample_rate),
            taps=None,
            fractional_bw=None,
            )

        self.dc_blocker_0 = filter.dc_blocker_cc(32, True)

        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        
        self.blocks_moving_average_0 = blocks.moving_average_ff(
            length=1000,
            scale=1,
            max_iter=1000
            )

        self.rational_resampler_recv_2 = filter.rational_resampler_fff(
            interpolation=1,
            decimation=int(self.int2_sample_rate/self.final_sample_rate),
            taps=None,
            fractional_bw=None,
            )
        
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_float*1, "localhost", self.data_port, 1472, True)
        ### end receiver blocks ###

        ### receiver connections ###
        self.connect((self.osmosdr_source_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.rational_resampler_recv_0, 0))
        self.connect((self.rational_resampler_recv_0, 0), (self.low_pass_filter_recv_0, 0))
        self.connect((self.low_pass_filter_recv_0, 0), (self.rational_resampler_recv_1, 0))
        #self.connect((self.blocks_head_0, 0), (self.low_pass_filter_recv_0, 0))
        #self.connect((self.low_pass_filter_recv_0, 0), (self.rational_resampler_recv_0, 0))
        #self.connect((self.rational_resampler_recv_0, 0), (self.rational_resampler_recv_1, 0))
        self.connect((self.rational_resampler_recv_1, 0), (self.dc_blocker_0, 0))
        self.connect((self.dc_blocker_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_moving_average_0, 0))
        self.connect((self.blocks_moving_average_0, 0), (self.rational_resampler_recv_2, 0))
        self.connect((self.rational_resampler_recv_2, 0), (self.blocks_udp_sink_0, 0))
        ### end receiver connections ###
        return


    def _setup_transmitter(self):
        ### transmitter extra parameters ###
        lpf_sample_rate = self.bandwidth*5 # pick a nice sample rate for the filter
        noise_source_gain = 5.0 # noise source block gain for the transmitter
        ### end transmitter extra parameters ###
        
        ### transmitter blocks ###
        self.analog_noise_source_0 = analog.noise_source_c(analog.GR_UNIFORM, noise_source_gain, 0)

        self.low_pass_filter_xmit_0 = filter.fir_filter_ccf(1, firdes.low_pass(
            1, lpf_sample_rate, self.bandwidth/2, self.transition, firdes.WIN_HAMMING, 6.76))

        self.rational_resampler_xmit_0 = filter.rational_resampler_ccc(
            interpolation=int(self.radio_sample_rate/lpf_sample_rate),
            decimation=1,
            taps=None,
            fractional_bw=None,
            )

        self.osmosdr_sink_0 = osmosdr.sink(args="numchan=1"+" "+self.radio_id)
        self.osmosdr_sink_0.set_sample_rate(self.radio_sample_rate)
        self.osmosdr_sink_0.set_center_freq(self.frequency+self.freq_offset, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(self.tx_rf_gain, 0)
        self.osmosdr_sink_0.set_if_gain(self.tx_if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(self.bandwidth, 0)
        ### end transmitter blocks ###

        ### transmitter connections ###
        self.connect((self.analog_noise_source_0, 0), (self.low_pass_filter_xmit_0, 0))
        self.connect((self.low_pass_filter_xmit_0, 0), (self.rational_resampler_xmit_0, 0))
        self.connect((self.rational_resampler_xmit_0, 0), (self.osmosdr_sink_0, 0))
        ### end transmitter connections ###
        return


