#loop12.py

number = int(raw_input("Enter an integer: "))
print("Factors:")
for x in xrange (1, number + 1):
    if number % x == 0:
        print (x) 
