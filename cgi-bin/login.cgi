#!/usr/bin/env python3

import cgi, cgitb

form = cgi.FieldStorage()

username = form.getvalue('uname')
password = form.getvalue('psw')


print(
"""Content-type: text/html

<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset="utf-8"/>
</head>
<body>

  <h1>You've Logged into the Antenna Range!</h1>

<h2>
Your username was:<br>""" + username + """ 
</h2>

<h2>
Your password was:<br>""" + password + """
</h2>



</body>
</html>
""")

