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

def adjust_pattern_size(theta, phi, masterDataPoints, armDataPoints):
    phi_min = phi[0]
    theta_min = theta[0]
    phi_max = math.pi
    
    #Adjust theta and phi so processing and graphing is easier
    theta_max = theta[-1]
    phi_ret, theta_ret = np.meshgrid(np.linspace(phi_min, phi_max, armDataPoints),
                                     np.linspace(theta_min, theta_max, masterDataPoints))
    return theta_ret, phi_ret
