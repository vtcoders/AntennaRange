#!/usr/bin/python


from MotorController import MotorController
from NetworkListener import NetworkListener
from PlotGraph import PlotGraph
from RadioFlowGraph import RadioFlowGraph
from RadioListener import RadioListener
from numpy import linspace
import sys
import time
import pdb
from pprint import pprint
import csv

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--ui":
	#varA = 1;
	#varB = 2;
	#varC = 3;
	#varD = (varA + varB)**varC;
	#pdb.set_trace();
        # interactive mode
        quit = False
        data = None
        while not quit:
            # show main menu
            menu_choices = []
            menu_choices.append("Run antenna pattern measurement scan")
            menu_choices.append("Plot last run data")
            menu_choices.append("Plot data from file")
            menu_choices.append("Quit")
            selection = show_menu(menu_choices)
            if selection == 1: #Run antenna measurement
                # prompt for scan parameters
                parameters = get_scan_parameters()
                data = do_scan(parameters)
                print(data)
            elif selection == 2: #Plot last run
                if data is None:
                    print("You must run a scan before plotting data!\n")
                    continue # cycle back to menu
                # plot the last run's data
                title = raw_input("Enter a title for the graph: ")
                plot_graph = PlotGraph(data, title)
                plot_graph.show()
            elif selection == 3: #Plot data from file
                fileName = raw_input("Enter the name of the data you want to plot\n")
                #fileName = "testdata.txt"
                fr = open(fileName)
                text = fr.readlines()
                fr.close()

                text.remove(text[0])

                dataPoint = 0
                fileData = []

                for dataString in text:
                    dataPointString = ''
                    dataTuple = []
                    for tempChar in dataString:
                        if tempChar == ',' or tempChar == '\n':
                            dataPoint = float(dataPointString)
                            dataTuple.append(dataPoint)
                            dataPointString = ''
                        else:
                            dataPointString += tempChar
                    fileData.append((dataTuple[0],dataTuple[1],dataTuple[2],dataTuple[3]))
                plot_graph = PlotGraph(fileData, fileName)
                plot_graph.show()
            elif selection == 4: #Quit
                print("Exiting...\n")
                quit = True
        return # exit since we're running in UI mode and user quit

    #Read from a config file, run on Tricorder, and send output file back to Rock
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as csvfile:    
            entry = csv.reader(csvfile, delimiter=',')
            
            for row in entry:
                #Header: frequency,mast_start_angle,mast_end_angle,mast_steps,arm_start_angle,arm_end_angle,arm_steps
                if row[0] == 'frequency' or row[0] == '':
                    continue
                params = read_config_file(row)

                if(params == None):
                    print("Config File not formatted properly. Exiting...\n")
                    return -1 #Indicate Failure
                
                #Run Antenna
                #TODO Find Proper location for SCP
                results = do_scan(params, str(sys.argv[1])) #mast_angle, arm_angle, background_rssi, transmission_rssi

                if(results == None):
                    print("Error on antenna itself. Exiting...\n")
                    return -2 #Indicate Failure

                #Plot Results
                #TODO Find Proper location for SCP
                plot_graph = PlotGraph(data, str(sys.argv[1]))
                plot_graph.savefig(str(sys.argv[1])+".png") 

            return 0 #Indicate success
    else:
        # network mode
        print("Network mode not yet operational, run with \"--ui\" for interactive mode.")
        # TODO finish networking



def get_scan_parameters():
	frequency = 2.32e9
	mast_start_angle = -180.0
	mast_end_angle = 180.0
	mast_steps = 181
	arm_start_angle = 0.0
	arm_end_angle = 0.0
	arm_steps = 1
 # get and validate each scan parameter from user
 #   frequency = -181.0
 #   while frequency < 30.0*1e6 or frequency > 6000.0*1e6:
 #   frequency = float(raw_input("Please enter the scan frequency in Hz (30*1e6 to 6000*1e6):   "))
 #   mast_steps = 0 # mast angle resolution 0.28 degrees (24/85 of a degree)
 #   while mast_steps < 1 or mast_steps > 1275:
 #   mast_steps = int(raw_input("Please enter the number of mast sampling steps (1 to 1275): "))
 #   mast_start_angle = -181.0
 #   while mast_start_angle < -180.0 or mast_start_angle > 180.0:
 #  mast_start_angle = float(raw_input("Please enter the mast starting angle (-180.0 to 180.0): "))
 #  mast_end_angle = -181.0
 #  while mast_end_angle < mast_start_angle or mast_end_angle > 180.0:
 #       mast_end_angle = int(raw_input("Please enter the mast ending angle (-180.0 to 180.0, >= starting angle): "))
 #    arm_steps = 0 # arm angle resolution 0.48 degrees
 #   while arm_steps < 1 or arm_steps > 750:
 #    arm_steps = int(raw_input("Please enter the number of arm sampling steps (1 to 1275, 1 for 2D scan): "))
 #   arm_start_angle = -181.0
 #   while arm_start_angle < -180.0 or arm_start_angle > 180.0:
 #       arm_start_angle = float(raw_input("Please enter the arm starting angle (-180.0 to 180.0, 0 for 2D scan): "))
 #   arm_end_angle = -181.0
 #   while arm_end_angle < arm_start_angle or arm_end_angle > 180.0:
 #       arm_end_angle = int(raw_input("Please enter the arm ending angle (-180.0 to 180.0, >= starting angle or 0 for 2D scan): "))
 #
	parameters = (frequency, mast_steps, mast_start_angle, mast_end_angle, arm_steps, arm_start_angle, arm_end_angle)
	return parameters

#Reads the inputted config file and validates input
def read_config_file(row):
    if len(row) < 7:
        print("Number of Parameters is Incorrect. See example file.")
        return None

    #Inputted Params
    frequency = float(row[0])
    mast_start_angle = float(row[1])
    mast_end_angle = float(row[2])
    mast_steps = float(row[3])
    arm_start_angle = float(row[4])
    arm_end_angle = float(row[5])
    arm_steps = float(row[6])

    #Validate each scan parameter from user
    if (frequency < 30.0*1e6 or frequency > 6000.0*1e6):
        print("Invalid frequency (30.0*1e6 to 6000.0*1e6)")
        return None
    if (mast_steps < 1 or mast_steps > 1275):# mast angle resolution 0.28 degrees (24/85 of a degree)
        print("Invalid mast sampling steps (1 to 1275)")
        return None
    if (mast_start_angle < -180.0 or mast_start_angle > 180.0):
        print("Invalid mast starting angle (-180.0 to 180.0)")
        return None
    if (mast_end_angle < mast_start_angle or mast_end_angle > 180.0):
        print("Invalid  mast ending angle (-180.0 to 180.0, >= starting angle)")
        return None
    if (arm_steps < 1 or arm_steps > 750): # arm angle resolution 0.48 degrees
        print("Invalid arm sampling steps (1 to 1275, 1 for 2D scan)")
        return None
    if (arm_start_angle < -180.0 or arm_start_angle > 180.0):
        print("Invalid arm starting angle (-180.0 to 180.0, 0 for 2D scan)")
        return None
    if (arm_end_angle < arm_start_angle or arm_end_angle > 180.0):
        print("Invalid arm arm ending angle (-180.0 to 180.0, >= starting angle or 0 for 2D scan)")
        return None

    #Properly formatted, return as tuple
    return (frequency, mast_steps, mast_start_angle, mast_end_angle, arm_steps, arm_start_angle, arm_end_angle)

def show_menu(choices):
    if choices == []:
        return None
    # print choices on screen
    row_num = 1
    print("\n\n\n")
    print("Please select from the following options:\n\n")
    for choice in choices:
        print(str(row_num)+": "+str(choice)+"\n")
        row_num += 1
    print("\n")
    # get response
    selection = 0
    while selection < 1 or selection > len(choices):
        selection = int(raw_input("Please enter your selection: "))
    return selection


def do_scan(parameters, inputFileName):
    frequency,mast_steps,mast_start_angle,mast_end_angle,arm_steps,arm_start_angle,arm_end_angle = parameters
    # perform a scan with the given sweep limits and step resolution
    net_listener = NetworkListener()
    net_listener.start()

    motor_controller = MotorController("/dev/ttyACM0", 115200)
    if motor_controller.connect():
        print("Successfully connected to motor controller.")
    else:
        print("Error: Motor controller not responding, verify connections.")
        return None
    motor_controller.reset_orientation()

    tx_radio_id = "hackrf=56a75f"
    rx_radio_id = "hackrf=61555f,buffers=4"
    #frequency = 914e6
    #frequency = 2.42e9
    tx_freq_offset = 0
    #rx_freq_offset = -5e3
    rx_freq_offset = -7e3
    data_port = 8888

    radio_listener = RadioListener()
    radio_listener.start()

    radio_tx_graph = RadioFlowGraph(tx_radio_id, frequency, tx_freq_offset, data_port)
    radio_tx_graph.set_tx_gain(14, 47)
    radio_tx_graph.setup_flowgraph(transmitter=True)
    radio_rx_graph = RadioFlowGraph(rx_radio_id, frequency, rx_freq_offset, data_port)
    radio_rx_graph.setup_flowgraph(transmitter=False)

    # open antenna scan log file and add data header
    filename_prefix = time.strftime("%d-%b-%Y_%H-%M-%S")
    filename = filename_prefix + "antenna_data_"+ inputFileName+".txt" #TODO Find Proper location for SCP
    datafile_fp = open(filename, 'w')
    datafile_fp.write("% Mast Angle, Arm Angle, Background RSSI, Transmission RSSI\n")
    antenna_data = []

    #mast_start_angle = -180.0
    #mast_end_angle = 180.0
    #mast_steps = 181 # >= 1
    #arm_start_angle = 0.0
    #arm_end_angle = 0.0
    #arm_steps = 1 # >= 1

    mast_angles = linspace(mast_start_angle, mast_end_angle, mast_steps)
    arm_angles = linspace(arm_start_angle, arm_end_angle, arm_steps)

    for mast_angle in mast_angles: # simulate n readings around antenna
        for arm_angle in arm_angles: # simulate n readings around antenna

            background_rssi = 0.0
            transmission_rssi = 0.0

            print("Target Mast Angle: "+str(mast_angle))
            print("Target Arm Angle: "+str(arm_angle))
            print("Moving antenna...")
            motor_controller.rotate_mast(mast_angle)
            motor_controller.rotate_arm(arm_angle)
            print("Movement complete")

            # background rssi reading
            print("Taking background noise sample...")
            radio_rx_graph.start()
            radio_rx_graph.wait()
            if radio_listener.is_data_available():
                background_rssi = radio_listener.get_data_average()
                print("Background RSSI: "+str(background_rssi))
            else:
                print("ERROR: Background RSSI unavailable!")
                return None
            #print("Sampling complete")

            # transmission rssi reading
            print("Taking transmitted signal sample...")
            radio_tx_graph.start()
            time.sleep(1.3) # give the transmitter flowgraph enough time to actually broadcast
            radio_rx_graph.start()
            radio_rx_graph.wait()
            radio_tx_graph.stop()
            radio_tx_graph.wait()
            if radio_listener.is_data_available():
                transmission_rssi = radio_listener.get_data_average()
                print("Transmission RSSI: "+str(transmission_rssi))
            else:
                print("ERROR: Transmission RSSI unavailable!")
                return None
            #print("Sampling complete")

            # write rssi readings to file
            print("Saving samples")
            datafile_fp.write(
                str(mast_angle) + ',' + 
                str(arm_angle) + ',' + 
                str(background_rssi) + ',' + 
                str(transmission_rssi) + '\n'
                )
            antenna_data.append((mast_angle, arm_angle, background_rssi, transmission_rssi))

    # return mast and arm to home position (0 degrees, 0 degrees)
    print("Returning mast and arm to home position...")
    motor_controller.rotate_mast(0)
    motor_controller.rotate_arm(0)
    print("Mast and arm should now be in home position")

    print("Scan completed, data saved in "+str(filename))

    radio_listener.stop()
    net_listener.stop()

    return antenna_data


if __name__ == "__main__":
    main()

