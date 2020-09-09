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

def adjust_pattern_size(theta, phi, dataPoints):
    phi_min = phi[0]
    theta_min = theta[0]
    phi_max = math.pi
    
    #Adjust theta and phi so processing and graphing is easier
    theta_max = theta[-1]
    phi_theta_ratio = round((phi_max - phi_min) / (theta_max - theta_min), 1)
    if phi_theta_ratio > 1:
        new_phi = int(round(dataPoints * phi_theta_ratio))
        new_theta = dataPoints
    else:
        new_theta = int(round(dataPoints / phi_theta_ratio))
        new_phi = dataPoints
    
    phi_ret, theta_ret = np.meshgrid(np.linspace(phi_min, phi_max, new_phi),
                                     np.linspace(theta_min, theta_max, new_theta))
    return theta_ret, phi_ret
