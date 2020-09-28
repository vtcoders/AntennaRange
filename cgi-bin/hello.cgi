#!/bin/bash

src="${BASH_SOURCE[0]}"
date="$(date)"

# Output an HTML5 page with the HTTP header being:
# Content-type: text/html\n\n

cat << EOF
Content-type: text/html


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
    $date
  </p>

  <p>
  The source to this script can be seen on this server in
  the file:<br>
  <i>$src</i>
  </p>

  <h2>And now for something very insecure</h2>

  <p>
    When this script just ran the following was so:
  </p>

  <ul>
     <li>user info=$(id)</li>
     <li>pwd=${PWD}</li>
     <li>env=<pre>$(env)</pre></li>
  </ul>

</body>
</html>
EOF
