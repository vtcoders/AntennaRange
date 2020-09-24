#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 06:42:47 2020
Surf2STL used to convert cartesian coordinates to
and stl file using ascii formatting
@author: Nick Tremaroli
"""
import numpy as np
import math
def surface2stl(X, Y, Z, filename):
    stlFile = open(filename, "w")
    stlFile.write("solid " + filename + "\r\n")
    
    numFaces = 0
    for i in range(len(Z) - 1):
        percent = (i / (len(Z) - 1)) * 100.0
        print(str(round(percent, 1)) + "%")
        for j in range(len(Z[0]) - 1):
            point1 = [X[i][j],         Y[i][j],         Z[i][j]]
            point2 = [X[i][j + 1],     Y[i][j + 1],     Z[i][j + 1]]
            point3 = [X[i + 1][j + 1], Y[i + 1][j + 1], Z[i + 1][j + 1]]
            numFaces = numFaces + writeFace(stlFile, point1, point2, point3)
            
            point1 = [X[i + 1][j + 1], Y[i + 1][j + 1], Z[i + 1][j + 1]]
            point2 = [X[i + 1][j],     Y[i + 1][j],     Z[i + 1][j]]
            point3 = [X[i][j],         Y[i][j],         Z[i][j]]
            numFaces = numFaces + writeFace(stlFile, point1, point2, point3)
            
    stlFile.write("endsolid " + filename + "\r\n")
    stlFile.close()
    return numFaces

def writeFace(stlFile, point1, point2, point3):
    precision = 2   # number of decimal points to round too
    if point1 is None or point2 is None or point3 is None:
        return 0
    n = findNormalLine(point1, point2, point3)
    if n[0] != "NaN" and n[1] != "NaN" and n[2] != "NaN":
        stlFile.write("facet normal " + str(round(n[0], precision)) + " " + str(round(n[1], precision)) + " " + str(round(n[2], precision)) + "\r\n")
    else:
        stlFile.write("facet normal NaN NaN NaN\r\n")
    stlFile.write("outer loop\r\n")
    stlFile.write("vertex " + str(round(point1[0], precision)) + " " + str(round(point1[1], precision)) + " " + str(round(point1[2], precision)) + "\r\n")
    stlFile.write("vertex " + str(round(point2[0], precision)) + " " + str(round(point2[1], precision)) + " " + str(round(point2[2], precision)) + "\r\n")
    stlFile.write("vertex " + str(round(point3[0], precision)) + " " + str(round(point3[1], precision)) + " " + str(round(point3[2], precision)) + "\r\n")
    stlFile.write("endloop\r\n")
    stlFile.write("endfacet\r\n")
    return 1
    
def findNormalLine(point1, point2, point3):
    v1 = [] * len(point1)
    v2 = [] * len(point1)
    for i in range(len(point1)):
        v1.append(point2[i] - point1[i])
        v2.append(point3[i] - point1[i])
    v3 = np.cross(v1, v2)
    n = []
    
    for i in range(len(v3)):
        if (v3[0] * v3[0] + v3[1] * v3[1] + v3[2] * v3[2]) == 0.0:
            n.append("NaN")
        else:
            n.append(v3[i] / math.sqrt(v3[0] * v3[0] + v3[1] * v3[1] + v3[2] * v3[2]))
            
    return n