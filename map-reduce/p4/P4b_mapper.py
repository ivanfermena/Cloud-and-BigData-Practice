#!/usr/bin/python3

import sys
import re

sums = {}
is_first = 1

for line in sys.stdin:

    if is_first:
        is_first = 0
        continue

    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r",", line)

    date_year = words[0][0:4]
    close = words[4]

    print( date_year + "\t" + close )
