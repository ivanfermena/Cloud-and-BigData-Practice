#!/usr/bin/python3

import sys
import re

sums = {}

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r' ', line)[6]
    print( words.lower() + "\t1")
