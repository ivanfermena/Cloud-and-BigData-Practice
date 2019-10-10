#!/usr/bin/python3

import sys
import re

for line in sys.stdin:

    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r",", line)

    meteorite_type = words[3]
    mass = words[4]

    if meteorite_type[0] != '"' and mass != "" and mass != "0": print( meteorite_type + "\t" + mass )