#loop5.py


import sys

amount = int(raw_input("How big of a square?"))

for x in xrange(0,amount):
    for y in xrange(0,amount):
        sys.stdout.write("*")
    print("")
