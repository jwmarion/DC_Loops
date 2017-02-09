#loop11.py
import sys

for x in xrange (2,10):
    for y in xrange (1, x):
        for z in xrange(0,y):
            sys.stdout.write("*")

        print("")
    print("")
