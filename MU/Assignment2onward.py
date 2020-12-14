"""
2.3 Write a program to prompt the user for hours and rate per hour using input
to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the
program (the pay should be 96.25). You should use input to read a string and
float() to convert the string to a number. Do not worry about error checking
or bad user data.
"""

# This first line is provided for you

hrs = input("Enter Hours:")
rate = input("Enter Pay:")
#pay = float(hrs) # method 1
x = float(hrs) * float(rate) # method 2

#print("Pay:", pay * float(rate)) # method 1
print("Pay:",x) # method 2


for i in range(5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)
