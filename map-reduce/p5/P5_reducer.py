#!/usr/bin/python3

import sys

previous = None
average = 0
num_element = 0

for line in sys.stdin:
    key, value = line.split( '\t' )
    
    if key != previous:
        if previous is not None:
            average = average/num_element
            print(previous + '\t' + str( average ))
            num_element = 0
        previous = key
        average = 0
    
    num_element = num_element + 1
    average = average + float( value )

average = average/num_element
print(previous + '\t' + str( average ))
