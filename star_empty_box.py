#loop6.py

import sys

width = int(raw_input("Width?: "))
height = int(raw_input("Height? "))


for x in xrange(0,height):
    for y in xrange(0, width):
        if (x == 0 or x == height -1):
            sys.stdout.write("*")
        else:
            if (y == 0 or y == width -1):
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")

    print("")
