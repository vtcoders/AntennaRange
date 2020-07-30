# RadioListener.py
# Listens for network connections from radio flowgraph and handles received data


import socket
import struct
import threading
from pprint import pprint


class RadioListener():
    def __init__(self, port=8888):
        if port < 1024:
            print("Error: Ports 0-1023 are reserved by the system and cannot be used.")
            return None
        self.port = int(port)
        self.time_to_exit = False
        self.data_points = []


    def start(self):
        # set up the UDP socket on the given interface address and port
        self.socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.settimeout(0.001)
        self.socket.bind(("localhost", self.port))
        # start a threaded listener
        self.listener_thread = threading.Thread(target=self._listen)
        self.listener_thread.start()
        print("Listener started")
        return


    def stop(self):
        self.time_to_exit = True # signal listener thread to stop accepting connections
        self.listener_thread.join() # wait for thread to finish
        print("Listener stopped")
        return


    def is_data_available(self):
        if len(self.data_points) > 0:
            return True
        else:
            return False


    #def get_data_point(self):
    #    return self.data_points.pop(0) # remove and return the first data point in the list


    #def get_all_data_points(self):
    #    return self.data_points


    def get_data_average(self):
        average = sum(self.data_points)/len(self.data_points)
        self.data_points = [] # clear data after calculations 
        return average


    def _listen(self):
        # we should only ever have 1 connection active at a time
        while not self.time_to_exit:
            try:
                data,address = self.socket.recvfrom(4096)
                while len(data) >= 4:
                    data_point, = struct.unpack("=f", data[0:4]) # gnuradio does NOT convert to network byte order!
                    self.data_points.append(data_point)
                    data = data[4:]
            except socket.timeout:
                pass
            except Exception as error:
                print("listener exception: "+str(error))
                if self.time_to_exit:
                    self.socket.close()


