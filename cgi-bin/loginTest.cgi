#!/usr/bin/env python3

import cgi, cgitb

form = cgi.FieldStorage()

username = form.getvalue('uname')
password = form.getvalue('psw')

# import pymongo

print(
"Content-type: text/html\n\n")

def fileToString(fileName):
    file = open(fileName)
    contents = file.read()
    file.close()
    return contents

print(fileToString("../AntennaRangeWebpage/home.html"))

