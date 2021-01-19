#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:22:24 2020
This file holds functions that can
be used to convert from the given coordinates to
and x3d file
@author: Nick Tremaroli
"""

def surface2x3d(X, Y, Z, gain, minGain, maxGain, precision, filename):
    
    x3dFile = open(filename, "w")
    # All of the inital data to start the top of the file
    x3dFile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    x3dFile.write("<X3D profile=\"Immersive\" version=\"3.2\">\n")
    x3dFile.write("\t<head>\n")
    x3dFile.write("\t\t<meta name=\"surf2x3d\" content=\"VT Antenna Range Project Conversion Program\"/>\n")
    x3dFile.write("\t</head>\n")
    x3dFile.write("\t<Material DEF=\"MA_Pelt\" transparency=\"0.0\"/>\n")
    x3dFile.write("\t<Scene>\n")
    x3dFile.write("\t\t<Transform>\n")
    x3dFile.write("\t\t\t<Group DEF=\"Plot\">\n")
    x3dFile.write("\t\t\t\t<Shape DEF=\"Antenna Range\">\n")
    

    coordIndexData = ""
    coordPointData = ""
    colorData = ""
    num = 0
    coordIndexFile = open(".coordIndexTemp", "w")
    coordPointFile = open(".coordPointTemp", "w")
    colorDataFile = open(".colorDataTemp", "w")
    for i in range(len(Z) - 1):
        percent = (i / (len(Z) - 1)) * 100.0
        print(str(round(percent, 1)) + "%")
        for j in range(len(Z[0]) - 1):
            coordIndexData = ""
            coordPointData = ""
            colorData = ""
            point1 = [X[i][j],         Y[i][j],         Z[i][j]]
            point2 = [X[i][j + 1],     Y[i][j + 1],     Z[i][j + 1]]
            point3 = [X[i + 1][j + 1], Y[i + 1][j + 1], Z[i + 1][j + 1]]
            
            coordPointData = coordPointData + str(round(point1[0], precision)) + " " + str(round(point1[1], precision)) + " " + str(round(point1[2], precision)) + ", "
            coordPointData = coordPointData + str(round(point2[0], precision)) + " " + str(round(point2[1], precision)) + " " + str(round(point2[2], precision)) + ", "
            coordPointData = coordPointData + str(round(point3[0], precision)) + " " + str(round(point3[1], precision)) + " " + str(round(point3[2], precision)) + ", "
            
            point1 = [X[i + 1][j + 1], Y[i + 1][j + 1], Z[i + 1][j + 1]]
            point2 = [X[i + 1][j],     Y[i + 1][j],     Z[i + 1][j]]
            point3 = [X[i][j],         Y[i][j],         Z[i][j]]
            
            coordPointData = coordPointData + str(round(point1[0], precision)) + " " + str(round(point1[1], precision)) + " " + str(round(point1[2], precision)) + ", "
            coordPointData = coordPointData + str(round(point2[0], precision)) + " " + str(round(point2[1], precision)) + " " + str(round(point2[2], precision)) + ", "
            coordPointData = coordPointData + str(round(point3[0], precision)) + " " + str(round(point3[1], precision)) + " " + str(round(point3[2], precision)) + ", "
            
            coordPointData = coordPointData + "\n"
            
            coordPointFile.write(coordPointData)
            
            ratio = 2 * (gain[i][j] - minGain) / (maxGain - minGain)
            blue = float(max(0, 1 * (1 - ratio)))
            red = float(max(0, 1 * (ratio - 1)))
            green = 1 - blue - red
            
            colorData = colorData + str(round(red, precision)) + " " + str(round(green, precision)) + " " + str(round(blue, precision)) + "\n"
            colorData = colorData + str(round(red, precision)) + " " + str(round(green, precision)) + " " + str(round(blue, precision)) + "\n"
            colorDataFile.write(colorData)
            
            coordIndexData = coordIndexData + str(num) + " " + str(num + 1) + " " + str(num + 2) + " -1\n"
            num = num + 3
            coordIndexData = coordIndexData + str(num) + " " + str(num + 1) + " " + str(num + 2) + " -1\n"
            num = num + 3
            
            coordIndexFile.write(coordIndexData)
            
    coordIndexFile.close()
    coordPointFile.close()
    colorDataFile.close()
    x3dFile.write("\t\t\t\t\t<IndexedFaceSet solid=\"false\" colorPerVertex= \"false\" coordIndex=\"\n")
    coordIndexFile = open(".coordIndexTemp", "r")
    lines = coordIndexFile.readlines();
    for line in lines:
        x3dFile.write(line)
    x3dFile.write("\">\n")
    coordIndexFile.close()
    
    x3dFile.write("\t\t\t\t\t<Color color=\"\n")
    colorDataFile = open(".colorDataTemp", "r")
    lines = colorDataFile.readlines();
    for line in lines:
        x3dFile.write(line)
    x3dFile.write("\"/>\n")
    
    x3dFile.write("\t\t\t\t\t<Coordinate point=\"")
    coordPointFile = open(".coordPointTemp", "r")
    lines = coordPointFile.readlines();
    for line in lines:
        x3dFile.write(line)
    x3dFile.write("\"/>\n")
        
    x3dFile.write("\t\t\t\t\t</IndexedFaceSet>\n")
    x3dFile.write("\t\t\t\t</Shape>\n")
    x3dFile.write("\t\t\t</Group>\n")
    x3dFile.write("\t\t</Transform>\n")
    x3dFile.write("\t</Scene>\n")
    x3dFile.write("</X3D>\n")
    
    x3dFile.close()



    



