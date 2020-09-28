#!/bin/bash

# Exit if the script fails due to error.
set -e

read_file="../uploads/tmp_file.html"

# Output an HTML5 page with the HTTP header being:
# Content-type: text/html\n\n

cat << EOF
Content-type: text/html

EOF
cat $read_file

