#!/usr/bin/env python3

import os
import datetime

date = str(datetime.datetime.now())
filename=__file__

# Output an HTML5 page with the HTTP header being:
# Content-type: text/html\n\n

print(
"""Content-type: text/html

<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset="utf-8"/>
</head>
<body>

  <h5><a href=".">toc</a></h5>

  <h1>Hello World!</h1>

  <p>
    The TIME on this server is:<br>
    """ + date + """
  </p>

  <p>
  The source to this script can be seen on this server in
  the file:<br>
  <i>""" + filename + """</i>
  </p>

</body>
</html>
""")
