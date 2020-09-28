#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 06:38:34 2020
antennaTo3d, now that more info
has been given to the team, we can now start the conversion
to an x3d file
@author: Nick Tremaroli
"""

#import necessary libraries needed for the conversion
import sys
import numpy as np
import matplotlib.pyplot as plt

import AntennaReader
import patternAdjuster
import surf2stl
import surf2x3d

if len(sys.argv) != 4:
    print("Error: incorrect number of arguements!")
    print("Call the program like: ./program <Input file> <File to output> <Binary value to show plot>")
    print("The input file must end with .txt or .csv")
    print("The output file must end with .stl or .x3d")
    
    print("\nExample: ./program input.txt output.x3d 0")
    sys.exit()

#Extract input arguments
inputFile = sys.argv[1]
outputFile = sys.argv[2]
showPlot = sys.argv[3]

#Make sure the input arguments are valid
if inputFile[-4:] != ".txt" and inputFile[-4:] != ".csv":
    print("Error: the input file must end in .txt or .csv!!")
    print("Call the program like: ./program <Input file> <File to output> <Binary value to show plot>")
    print("Example: ./program input.txt output.x3d 0")
    sys.exit()

if outputFile[-4:] != ".stl" and outputFile[-4:] != ".x3d":
    print("Error: the output file must end in .stl or .x3d!!")
    print("Call the program like: ./program <Input file> <File to output> <Binary value to show plot>")
    print("Example: ./program input.txt output.x3d 0")
    sys.exit()
    
if showPlot != "1" and showPlot != "0":
    print("Error: the plot value must be either a 1 or a 0!!")
    print("Call the program like: ./program <Input file> <File to output> <Binary value to show plot>")
    print("Example: ./program input.txt output.x3d 0")
    sys.exit()

#np.set_printoptions(threshold=sys.maxsize)
# ^ uncomment for debugging purposes to print the data matrix fully

#Read the input file
antennaReader = AntennaReader.AntennaReader(inputFile)
antennaReader.ReadEntireFile()

armAngles = antennaReader.GetArmAngle()

masterAngles = antennaReader.GetMasterAngle()
masterAngleDataPoints = 1
firstMasterValue = masterAngles[0]

for i in range(len(masterAngles)):
    if firstMasterValue != masterAngles[i + 1]:
        masterAngleDataPoints = masterAngleDataPoints + 1
    else:
        break

#Get the raw gain from the input file
rawGain = antennaReader.GetTransmissionRSSI()
armAngleDataPoints = int(len(rawGain) / masterAngleDataPoints)

#Setup theta and phi for spherical coordinate graphing
theta, phi = np.linspace(0, 2 * np.pi, int(masterAngleDataPoints)), np.linspace(0, np.pi * 89/90, armAngleDataPoints)

theta, phi = patternAdjuster.adjust_pattern_size(theta, phi, masterAngleDataPoints, armAngleDataPoints)

#the actual gain that will be used for processing
gain = [[0.0 for i in range(len(phi[0]))] for j in range(len(phi))]


#if its an x3d calculate max and min now to save processing time
minGain = 0.0
maxGain = 0.0
if outputFile[-4:] == ".x3d":
    for i in range(len(gain[0])):
        for j in range(len(gain)):
            index = (i * masterAngleDataPoints) + j
            #logatithmic normalization
            if index < len(rawGain):    
                gain[j][i] = 10 * (rawGain[index] + 20)
            else:
                gain[j][i] = 10 * (rawGain[-1] + 20)
                    
            if gain[j][i] < 0.0:
                gain[j][i] = 0.0
            
            #find max and min
            if gain[j][i] < minGain:
                minGain = gain[j][i]
            if gain[j][i] > maxGain:
                maxGain = gain[j][i]
else:
    for i in range(len(gain[0])):
        for j in range(len(gain)):
            index = (i * masterAngleDataPoints) + j
            #logatithmic normalization
            if index < len(rawGain):    
                gain[j][i] = 10 * (rawGain[index] + 20)
            else:
                gain[j][i] = 10 * (rawGain[-1] + 20)
                    
            if gain[j][i] < 0.0:
                gain[j][i] = 0.0


#for pathing the slot
for i in range(int(len(gain) / 2)):
    temp = gain[i][len(gain[i]) - 1]
    gain[i][len(gain[i]) - 1] = gain[len(gain) - i - 1][len(gain[i]) - 1]
    gain[len(gain) - i - 1][len(gain[i]) - 1] = temp
    
#Convert the gain to a numpy array for easier processing
gain = np.array(gain)

#Convert from spherical coordinates to cartesian coordinates
X = gain * np.sin(theta) * np.cos(phi)
Y = gain * np.sin(theta) * np.sin(phi)
Z = gain * np.cos(theta)


#Show the plot based on the input argument
if showPlot == "1":
    print("Displaying plot!")
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    
    plot = ax.plot_surface(
        X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('jet'),
        linewidth=0, antialiased=False, alpha=0.5)
    
    plt.show()

#Create either an stl or an x3d based on the file extension of the output file
if outputFile[-4:] == ".stl":
    print("Now converting \"" + inputFile + "\" to the stl file!: " + outputFile)
    surf2stl.surface2stl(X, Y, Z, outputFile)
elif outputFile[-4:] == ".x3d":
    print("Now converting \"" + inputFile + "\" to x3d file!: " + outputFile)
    surf2x3d.surface2x3d(X, Y, Z, gain, minGain, maxGain, outputFile)
else:
    print("Error trying to create the output file: " + outputFile)
    sys.exit()

print("Done!")