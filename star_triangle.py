#loop7.py

import sys
xr = 5

for x in xrange (0, xr):
    for y in xrange (0, xr - (x+1)):
        sys.stdout.write(" ")
    for z in xrange (0, x * 2 + 1):
        sys.stdout.write("*")
    for a in xrange (0, xr - (x + 1)):
        sys.stdout.write(" ")
    print ""
