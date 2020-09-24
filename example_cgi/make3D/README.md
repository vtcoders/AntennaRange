Antenna Range Project 3D printing Team

The main file to run is antennaTo3d.py

This program written in python 3.8 is used
to take an antenna range descritpion file
in the form of a .txt or a .csv and converts
it to a 3D file.

The 3D files that are supported are .stl and .x3d

RECOMMENDATION!!: If the 3D file you are generating has the SOLE purpose
of being 3D printed, it is RECOMMENDED (not necessary) that you convert the
data to a .stl file as it takes up less hard drive space and takes less time to
process than an x3d because it does not include color data (which is not
needed if you are just 3D printing). On the other hand, if you are uploading
this 3D file to a website and NEED color data, convert it to a .x3d file

Call the program like:
./antennaTo3d.py 'Input file' 'File to output' 'Binary value to show plot'

The input file is the file that has the raw antenna range data. This file MUST
END with either .txt or .csv in order to be correctly read

The code reads the .txt or .csv and only really looks at the master angle and the gain. The program MUST have equal step sizes for the master angle and the arm angle as the current calculation and evaluation of the data requires it to be so. While reading the input, the program notices how many master angle data points there are (before they start to repeat) and divides it by the number of gain data points. This number that results is used to assume how many different arm angle data points there are. As a result, the arm angle step size is assumed and if every measurement is sequential and increases at a constant step size, this mathematical shortcut holds valid and produces the same result. Hence, the program does NOT look at the arm angle column and you will notice that some of the .csv files in the final product folder have constant arm angles that do not change, but in reality, the program is automatically calculating the arm angle step size based on how many data points there are. This mathematical shortcut can be easily removed and each data point can be read and evaluated, the team just thought this shortcut could save the user some time and if all the input data has sequential step sizes that this shortcut wouldn't be an issue.

The output file is the 3D file that is generated. This file MUST END with
either .stl or .x3d. The program will automatically check the file
extension you inputted and format it correctly for that file extension

The Binrary Value to show the plot can either be 1 or 0 and is used for
debugging purposes. If set to 1, the program will display a plot of the
antenna pattern before converting the data to a 3D file. Once the user closes
out the plot, the program continues as normal
