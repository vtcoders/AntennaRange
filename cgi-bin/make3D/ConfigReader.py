#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:58:43 2020

@author: n
"""
import sys
import csv
import Constants

class ConfigReader:
    
    def __init__(self, filename):
        self.filename = filename
        self.configFile = open(self.filename, "r")
        if self.configFile.mode != "r":
            print("Error could not read the config file")
            sys.exit()
    
        self.mastStartAngle = 0
        self.mastEndAngle = 0
        self.mastSteps = 0
        self.armStartAngle = 0
        self.armEndAngle = 0
        self.armSteps = 0
    
    def ReadEntireFile(self):
        
        parser = csv.reader(self.configFile)
        next(parser)
        row = next(parser)
        
        self.mastStartAngle = float(row[Constants.MAST_START_INDEX])
        self.mastEndAngle = float(row[Constants.MAST_END_INDEX]) 
        self.mastSteps = int(row[Constants.MAST_STEPS_INDEX])
        
        self.armStartAngle = float(row[Constants.ARM_START_INDEX])
        self.armEndAngle = float(row[Constants.ARM_END_INDEX])
        self.armSteps = int(row[Constants.ARM_STEPS_INDEX])
        
    def GetMasterStartAngle(self):
        return self.mastStartAngle

    def GetMasterEndAngle(self):
        return self.mastEndAngle

    def GetMasterAngleSteps(self):
        return self.mastSteps

    def GetArmStartAngle(self):
        return self.armStartAngle

    def GetArmEndAngle(self):
        return self.armEndAngle

    def GetArmAngleSteps(self):
        return self.armSteps        