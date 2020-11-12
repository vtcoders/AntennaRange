#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 08:57:21 2020
Antenna_ploter has function used to help plot
the antenna range
@author: Nick Tremaroli
"""

import math
import numpy as np

def GetAngles(mastStart, mastEnd, mastDataPoints, armStart, armEnd, armDataPoints):
#    phi_min = phi[0]
#    theta_min = theta[0]
#    phi_max = math.pi * 2
    
    #Adjust theta and phi so processing and graphing is easier
#    theta_max = theta[-1]
    mastStart = (mastStart * math.pi) / 180.0
    mastEnd = (mastEnd * math.pi) / 180.0


    armStart = (armStart * math.pi) / 180.0
    armEnd = (armEnd * math.pi) / 180.0
    armAngles, mastAngles = np.meshgrid(np.linspace(armStart, armEnd, armDataPoints),
                                     np.linspace(mastStart, mastEnd, mastDataPoints))
    return mastAngles, armAngles

def GetMastAngles(mastStartAngle, mastEndAngle, mastSteps):
    return np.linspace(mastStartAngle, mastEndAngle, mastSteps)

def GetArmAngles(armStartAngle, armEndAngle, armSteps):
    return np.linspace(armStartAngle, armEndAngle, armSteps)