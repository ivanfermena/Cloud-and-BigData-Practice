#!/usr/bin/python3

import sys

print("Lines:")

for line in sys.stdin:
    key, value = line.split( '\t' )
    print(value)