""" Muhammad Khan
Exercise 2: Write a program that prompts the user
for their name. When they respond, write their
name to a file called “guest.txt”.

name = input("Enter your name: ")
fout = open("pythonPrac.txt", "a")
fout.write(name)
fout.close()
print("Value assigned")
"""

"""
# This is a read() method for a file located in the same folder as Python.
f = open("pythonPrac.txt", "r")
print(f.read())
"""

"""
# If the file is located in a different location, you will have to specify the file path, like this:
myfile = open(r"C:ucbil\OneDrive\Desktop\Checking.txt") # notice the "r" before the path. Very important!!!!
print(myfile.read()) # This is a normal text file

mystr = open(r"ucbil\OneDrive\Documents\QCC\ET-710 Web Technology\json.txt")
print(mystr.read()) # However, this is a JSON file, yet it still prints in the very same manner.
 """

"""
# you can also specify how many characters you want to return in a read() method
f = open("pythonPrac.txt", "r")
print(f.read(10)) # The output is "Muhammad B" because im asking for only 9 chars
"""

"""
f = open("pythonPrac.txt", "r")
print(f.readline()) # it prints out only 1 line
"""

"""
f = open("pythonPrac.txt", "r")
for x in f: # Looping also works
    print(x)
"""

"""
# It is a good practice to always close the file when you are done with it
f = open("pythonPrac.txt", "r")
print(f.readline())
f.close()
"""

"""
# Add a parameter to the open() function to write to an existing file
f = open("pythonPrac.txt", "a") # "a" will append to the end of the file
f.write("This should be another one.\n")
f.close()

f = open("pythonPrac.txt", "r") #open and read the file after the appending
print(f.read())
"""

"""
# the "w" method will overwrite the entire file.
f = open("pythonPrac.txt", "w")  # "w" - Write - will overwrite any existing content
f.write("Every previous chars have been replaced by this one.")
f.close()

f = open("pythonPrac.txt", "r")
print(f.read())
"""


# Left a create a new file https://www.w3schools.com/python/python_file_write.asp
