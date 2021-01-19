#!/usr/bin/env python3

import cgi, cgitb

form = cgi.FieldStorage()

print(
"""Content-type: text/html

<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset="utf-8"/>
</head>
<body>


<h1>
Sorry, This feature is yet to be fully implemented but will be soon!
</h1>



</body>
</html>
""")
