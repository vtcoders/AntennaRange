#!/usr/bin/env python3

import cgi, cgitb

form = cgi.FieldStorage()

import pymongo
#install mongoDB on the computer
#pip install pymongo
from pymongo import MongoClient

#connects to local mongoDB on my machine
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#used for grabbing a database
mydb = myclient["mydatabase"]

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
