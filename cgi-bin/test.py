#!/usr/bin/env python3

import cgi, cgitb

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

