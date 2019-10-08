#!/usr/bin/python3

import sys
import re

sums = []
is_first = 1

for line in sys.stdin:

    if is_first:
        is_first = 0
        continue

    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r",", line)

    id_movie = words[1]
    ratings = words[2]

    #sums.append({ id_movie: ratings })
    print( id_movie + "\t" + ratings )

#print(sums)
