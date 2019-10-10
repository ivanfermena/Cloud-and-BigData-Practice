#!/usr/bin/python3

import sys
import re

for line in sys.stdin:

    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r",", line)

    date_year = words[0][0:4]
    close = words[4]

    print( date_year + "\t" + close )
