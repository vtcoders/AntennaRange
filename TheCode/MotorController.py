# MotorController.py
# Handles motor controller interface and commands


import serial
import time
from pprint import pprint


class MotorController():
    # configuration parameters


    def __init__(self, serial_device, baudrate):
        self.serial_device = serial_device
        self.serial_baudrate = baudrate
        self.connection = None
        self.mast_angle = 0.0
        self.arm_angle = 0.0


    def connect(self):
        #self.connection = serial.Serial(self.serial_device, self.serial_baudrate, timeout=1)
        self.connection = serial.Serial()
        self.connection.port = self.serial_device
        self.connection.baudrate = self.serial_baudrate
        self.connection.timeout = 1
        self.connection.dtr = 0 # don't reset microcontroller when connecting
        self.connection.open()
        connect_msg = ""
        connect_tries = 10
        while connect_msg.strip() == "" and connect_tries > 0:
            connect_msg = self.connection.readline()
            connect_tries = connect_tries - 1 
        print("Connect response: "+connect_msg)
        # restrict movement rate (feedrate) to 500 units per second
        self.connection.write("G1 F500\n")
        response = self.connection.readline()
        print("Set feedrate response: "+response)
        if connect_msg.find("Grbl 1.1f") < 0 or connect_tries == 0 or response[:2] != "ok":
            self.connection = None
            return False
        else:
            self.connection.reset_input_buffer()
            self.connection.reset_output_buffer()
            return True


    def disconnect(self):
        self.connection.close()
        self.connection = None


    def is_connected(self):
        if self.connection is not None:
            return self.connection.is_open
        else:
            return False


    def _get_controller_angles(self):
        # get the current angles (position) from the controller firmware
        self.connection.write("?")
        response = self.connection.readline()
        # find the MPos data segment
        mpos = ""
        found = False
        for part in response.split("|"):
            if part.find("MPos") == 0:
                mpos = part
                found = True
        if found:
            # extract angles from the data segment "MPos:x,y,z"
            mast_angle = mpos.split(":")[1].split(",")[0]
            arm_angle = mpos.split(":")[1].split(",")[1]
            return (mast_angle, arm_angle)
        else:
            return None


    def get_current_angles(self):
        return (self.mast_angle, self.arm_angle)


    def _send_movement_command(self, axis, amount):
        # send actual movement command
        self.connection.write("G1 "+axis+str(amount)+"\n")
        response1 = self.connection.readline()
        print("Move response: "+response1)
        if response1[:5] == "error":
            return False
        # send "wait for last movement to complete" command
        self.connection.write("G4 P0\n")
        timeout = 30 # seconds
        start_time = time.clock()
        stop_time = start_time
        while (stop_time - start_time) < timeout:
            response2 = self.connection.readline()
            print("Wait response: "+response2)
            if response2[:5] == "error":
                return False
            elif response2[:2] == "ok":
                return True
        # if we got this far we timed out waiting for a response
        return False


    def rotate_mast(self, degrees):
        # rotate the mast (upright portion) by the given number of degrees,
        # X axis, positive values for CW, negative for CCW 
        # (as seen when looking from top of mast downwards)
        amount = degrees
        if self._send_movement_command("X", amount):
            self.mast_angle += degrees
            return True
        else:
            return False


    def rotate_arm(self, degrees):
        # rotate the arm (lengthwise portion)  by the given number of degrees,
        # Y axis, positive values for CW, negative for CCW 
        # (as seen when looking from outer end of arm towards mast)
        amount = degrees
        if self._send_movement_command("Y", amount):
            self.arm_angle += degrees
            return True
        else:
            return False


    def _reset_angles(self):
        # reset the controller angles (position)
        self.connection.write("G92.1\n")
        response = self.connection.read(4)
        if response != "ok\r\n":
            return False
        else:
            # reset our internal angles
            self.mast_angle = 0.0
            self.arm_angle = 0.0
            return True


    def _send_homing_command(self):
        return True # TODO remove when homing sensors installed
        # send the homing command to the controller
        self.connection.write("$H\n")
        response = self.connection.read(4)
        if response != "ok\r\n":
            return False
        else:
            return True


    def reset_orientation(self):
        return self._send_homing_command() and self._reset_angles()


