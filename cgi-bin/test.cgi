#!/usr/bin/env python3

import cgi, cgitb, sys

from os.path import dirname
# sys.path.append(os.path.dirname(__file__))
sys.path.append("/home/tim23/.local/lib/python3.6/site-packages")

form = cgi.FieldStorage()

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

