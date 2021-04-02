#!/usr/bin/env python3

import cgi, cgitb

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

