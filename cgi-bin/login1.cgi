#!/usr/bin/env python3

import cgi, cgitb

form = cgi.FieldStorage()

username = form.getvalue('uname')
password = form.getvalue('psw')

# import pymongo

def displaySuccessful():


_usernameFound=True
_passwordCorrect=False

if (_usernameFound and _passwordCorrect):
    displaySuccessful()
else:
    displayUnsuccessful()



print(
"""Content-type: text/html

<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset="utf-8"/>
</head>
<body>

<h1 style="color:white;background-color:black">Hello """ + username + """!</h1>

<h2>
Thank you for logging on to the Antenna Range! This feature is yet to be fully implemented but will be soon!
</h2>



</body>
</html>
""")

