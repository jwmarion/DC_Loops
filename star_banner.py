#loop10.py

import sys

mess = raw_input("What would you like on the banner?")

mlen = len(mess)

def fillout(num):
    for x in xrange(0,num+2):
        sys.stdout.write("*")
    print("")


fillout(mlen)
print "*%s*" % mess
fillout(mlen)
