#!/usr/bin/env python3

import cgi, cgitb, sys
# sys.path.append(os.path.dirname(__file__))
# MAY NEED TO FIX LATER, IT SEEMS LIKE THIS IS OK AS LONG AS THIS IS IN
# CGI-BIN AND EVERYONE'S DIRECTORY STRUCTURE IS THE SAME
filepath = "../../.local/lib/python3.6/site-packages"
sys.path.append(filepath)

form = cgi.FieldStorage()

import sys
sys.path.append("/home/arjun24/.local/lib/python3.6/site-packages/")

import pymongo


print(
"""Content-type: text/html

<!DOCTYPE html>
<html lang=en>
<head>
</head>
<body>

  <h1>Antenna Range!</h1>

</body>
</html>
""")

