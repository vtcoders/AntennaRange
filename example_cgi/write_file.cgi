#!/bin/bash

# Exit if the script fails due to error.
set -e



create_file="/home/www-data/lance/tmp_file.html"


src="${BASH_SOURCE[0]}"
dir="$(dirname $src)"
cd "$dir"
this_file="$(basename $src)"

date="$(date)"

# Output an HTML5 page with the HTTP header being:
# Content-type: text/html\n\n

cat > "$create_file" << EOF
<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset="utf-8"/>
</head>
<body>

  <h5><a href=".">toc</a></h5>

  <p>
    This is the file that was created by the script at
    <a href="./${this_file}">$dir/${this_file}</a>.
  </p>

  <p>
    The TIME this file was created is:
    <pre>$date</pre>
  </p>

  <p>
    You may need to do a <i>&lt;SHIFT&gt;reload</i> to
    see the latest version of this file.

</body>
</html>
EOF


cat << EOF
Content-type: text/html


<!DOCTYPE html>
<html lang=en>
<head>
  <meta charset="utf-8"/>
</head>
<body>

  <h5><a href=".">toc</a></h5>

  <h2>We just did something very insecure</h2>

  <p>
    We just wrote the file: ${create_file}<br>
    You can read the file with: <a
       href="read_file.cgi">read_file.cgi</a>.
  </p>

</body>
</html>
EOF
