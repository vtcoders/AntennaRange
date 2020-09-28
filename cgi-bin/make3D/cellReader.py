#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 05:30:17 2020
Cell Reader: Used to extract important data from
the excel file
@author: Nick Tremaroli
"""

import re                    # for regular expression processing

def GetGains(excelFile):
    location = ""
    letter = ""
    
    #find where the gain is located
    for j in range(excelFile.number_of_columns()):
        letter = chr(65 + j)
        for i in range(excelFile.number_of_rows()):
            location = letter + str(i)
            if str(excelFile[location]).lower() == "gain":
                break
                
    #find where the gain values start (shouldn't be to far from the cell where gain was located)
    while re.match(r'^-?\d+(?:\.\d+)?$', str(excelFile[location])) is None:
        i = int(location[1:])
        i = i + 1;
        location = letter + str(i)
        
    gain_1 = []
    while re.match(r'^-?\d+(?:\.\d+)?$', str(excelFile[location])) is not None:
        gain_1.append(excelFile[location])
        i = int(location[1:])
        i = i + 6
        location = letter + str(i)
    
    #find where the gain is located
    for j in range(excelFile.number_of_rows()):
        i = i + 1
        location = letter + str(i)
        if str(excelFile[location]).lower() == "gain":
            break
    
    #find where the gain values start (shouldn't be to far from the cell where gain was located)
    while re.match(r'^-?\d+(?:\.\d+)?$', str(excelFile[location])) is None:
        i = int(location[1:])
        i = i + 1
        location = letter + str(i)
        
    gain_2 = []
    while re.match(r'^-?\d+(?:\.\d+)?$', str(excelFile[location])) is not None and i < excelFile.number_of_rows():
        gain_2.append(excelFile[location])
        i = int(location[1:])
        if i + 6 >= excelFile.number_of_rows():
            break
        i = i + 6
        location = letter + str(i)
    
    return gain_1, gain_2

