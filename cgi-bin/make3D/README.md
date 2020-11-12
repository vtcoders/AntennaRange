Antenna Range Project 3D printing Team

The main file to run is antennaTo3d.py

This program written in python 3.8 is used
to take an antenna range descritpion file
in the form of a .txt or a .csv and converts
it to a 3D file.

The 3D files that are supported are .stl and .x3d

RECOMMENDATION!!: If the 3D file you are generating has the SOLE purpose
of being 3D printed, it is RECOMMENDED that you convert the
data to a .stl file as it takes up less hard drive space and takes less time to
process than an x3d because it does not include color data (which is not
needed if you are just 3D printing). On the other hand, if you are uploading
this 3D file to a website and NEED color data, convert it to a .x3d file

UPDATE REGARDING STL EXPORT
Most antenna ranges tend to have a singularity point which is an
infintly small point that could potentialy seperate two seperate parts
of the antenna range. If your desire is to 3D print the antenna range, this
will be difficult as the part around the singularity point is weak and will
break extremly easy. HENCE, to account for this, the code has been reprogrammed
so that when you export to an STL FILE ONLY, there is some artifical material
around the singularity point that has been added so the 3D printer can print
an antenna range successfully without any issues. The shape of this artificial
material is a sphere and the size of the sphere can be adjusted in the Constants.py
file

Call the program like:
./antennaTo3d.py 'Config File' 'Input file' 'File to output' 'Prescision place number' 'Binary value to show plot'

The config File is the file used by the positioner program, it is a 2 row csv file
which specifies the start and stop angles for both the master and arm angle respectivly
This config file is used to prevent unneccessary parsing through the input file


The input file is the file that has the raw antenna range data. This file MUST
END with either .txt or .csv in order to be correctly read


The output file is the 3D file that is generated. This file MUST END with
either .stl or .x3d. The program will automatically check the file
extension you inputed and format it correctly for that file extension

The Prescision placement number is a number that is used to specify how
many decimal places the data should be rounded too when exporting an x3d
or an stl. 1 for tenths place, 2 for hundreths place, etc. Increase this number
for a more accurate representation of the antenna range but note that as this
number increases, so will the size of the exported stl or x3d file.

The Binary Value to show the plot can either be 1 or 0 and is used for
debugging purposes. If set to 1, the program will display a plot of the
antenna pattern before converting the data to a 3D file. Once the user closes
out the plot, the program continues as normal

