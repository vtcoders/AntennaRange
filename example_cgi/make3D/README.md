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
./antennaTo3d.py 'Input file' 'File to output' 'Quality %' 'Binary value to show plot'

The input file is the file that has the raw antenna range data. This file MUST
END with either .txt or .csv in order to be correctly read

The output file is the 3D file that is generated. This file MUST END with
either .stl or .x3d. The program will automatically check the file
extension you inputted and format it correctly for that file extension

The Quality % was made for the purpose of saving time and space. The Quality % is a
percentage of how many of the data points provided (in the input file) will
actually be used to generate the output file. This was made to give the
user the OPTION to slightly lower the quality of the 3D shape so that stl and
x3d file can still have the relative shape of the antenna pattern while taking
up less space on the hard drive and taking less time to process through
this program. Regardless of how low the quality % is set, there will always
be at least 30 data points used by the program. So you use all of the data
points, this value should be 100, to use have of them, this value should be 50

The Binrary Value to show the plot can either be 1 or 0 and is used for
debugging purposes. If set to 1, the program will display a plot of the
antenna pattern before converting the data to a 3D file. Once the user closes
out the plot, the program continues as normal