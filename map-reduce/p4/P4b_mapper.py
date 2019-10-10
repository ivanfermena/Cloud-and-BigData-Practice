#!/usr/bin/python3

import sys
import re

sums = {}
key_range = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    value = float(value)

    if value <= 1: key_range = 1
    elif value <= 2: key_range = 2
    elif value <= 3: key_range = 3
    elif value <= 4: key_range = 4
    elif value <= 5: key_range = 5

    print( str(key_range) + "\t" + key )
    