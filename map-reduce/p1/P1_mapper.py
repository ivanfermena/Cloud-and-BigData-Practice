#!/usr/bin/python3

import sys
import re

count_lines = 0
word_search = sys.argv[1].lower()
sums = {}

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)
    
    for word in words:
        word = word.lower()
        if word == word_search:
            print( word + "\t" + line )