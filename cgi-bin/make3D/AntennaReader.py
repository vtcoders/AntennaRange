#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:16:26 2020
A script used to get all of the valuable information
from the txt file describing the antenna range
@author: Nick Tremaroli
"""
import sys
import csv
class AntennaReader:
    #Initalize and get the antenna data from the file
    def __init__(self, filename):
        self.filename = filename
        self.antennaRangeFile = open(self.filename, "r")
        if self.antennaRangeFile.mode != "r":
            print("Error could not read the antenna range file")
            sys.exit()
            
        self.masterAngle = []
        self.armAngle = []
        self.backgroundRSSI = []
        self.transmissionRSSI = []
    
    #For now it is assumed the input file is formatted like:
    #master angle, arm angle, Background RSSI, Transmission RSSI
    def ReadEntireFile(self):
        for row in csv.reader(self.antennaRangeFile):
            
            allDigits = True
            for item in row:
                temp = item.replace('.', '', 1) 
                temp = temp.replace('-', '', 1)
                if temp.isdigit() is False:
                    allDigits = False
                    break
                
            if allDigits is True:
                self.masterAngle.append(float(row[0]))
                self.armAngle.append(float(row[1]))
                self.backgroundRSSI.append(float(row[2]))
                self.transmissionRSSI.append(float(row[3]))
    
    
    def GetMasterAngle(self):
        return self.masterAngle
    
    def GetArmAngle(self):
        return self.armAngle
    
    def GetBackgroundRSSI(self):
        return self.backgroundRSSI
    
    def GetTransmissionRSSI(self):
        return self.transmissionRSSI