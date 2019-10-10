#!/usr/bin/python3

import sys
import re

sums = []

for line in sys.stdin:

    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r",", line)

    id_movie = words[1]
    ratings = words[2]

    print( id_movie + "\t" + ratings )
