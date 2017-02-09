#loop8.py

import sys
xr = int(raw_input("Enter a height (integer)"))

def spaces (current):
    for y in xrange (0, xr - (current+1)):
        sys.stdout.write(" ")

def stars (current):
        for z in xrange (0, current * 2 + 1):
            sys.stdout.write("*")


for x in xrange (0, xr):
    spaces(x)
    stars(x)
    spaces(x)
    print ""
