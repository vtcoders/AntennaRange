# NetworkListener.py
# Listens for network connections and handles message formatting and parsing


import socket
#import twisted


class NetworkListener():
    def __init__(self, host_address="", port=8000):
        if port < 1024:
            print("Error: Ports 0-1023 are reserved by the system and cannot be used.")
            return None
        # set up a TCP listener on the given interface address and port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host_address, port))



    def start(self):
        pass


    def stop(self):
        pass


