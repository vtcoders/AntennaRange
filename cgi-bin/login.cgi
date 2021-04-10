#!/usr/bin/env python3

import cgi, cgitb, sys

form = cgi.FieldStorage()

username = form.getvalue('uname')
password = form.getvalue('psw')

filepath = "../../.local/lib/python3.6/site-packages"
sys.path.append(filepath)

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["test"]
mycol = mydb["accounts"]

myquery = {"username": username}

account = mycol.find_one(myquery)

printString = ""
if (account == None or account['password'] != password):
  printString = "The username or password is incorrect, please try again."
else:
  printString = "Hello " + account['name'] + "!"


print(
"""Content-type: text/html

<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset="utf-8"/>
</head>
<body>

<h1 style="color:white;background-color:black">""" + printString + """!</h1>

<h2>
Thank you for logging on to the Antenna Range! This feature is yet to be fully implemented but will be soon!
</h2>



</body>
</html>
""")
