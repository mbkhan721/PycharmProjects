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

"""
f = open("myfile.txt", "a")
f.write("This file was just created.\nThis line is just added to it")
f.close()
print("Characters added!")
"""

"""
f = open("myfile.txt", "w")
f.write("This code is jsut added to the new file.\nReplacing the old one.")
f.close()
"""

# To delete a file
"""
import os
os.remove("myfile.txt")
"""

# Check if file exists, then delete it
"""
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("This file does not exits")

    
# Remove the folder "myfolder"

# import os
# os.rmdir("myfolder")

# You can only remove empty folders
"""

# Exercise 1
""" Open a blank file in your text editor and write a few lines
summarizing what you’ve learned about Python so far.
Start each line with the phrase In Python you can.... Save
the file as learning_python.txt in the same directory as your
exercises from this chapter.
• Write a program that reads the file and prints what you
wrote three times.
• Print the contents once by reading in the entire file, once
by looping over the file object, and once by storing the
lines in a list and then working with them outside the with
block. """
"""
file = open("pythonPrac.txt", "r")
print("* Reading in the entire file:\n", file.read())
file.close()

print("\n* Looping over the file objects:")
file = open("pythonPrac.txt", "r")
for i in file:
    print(i.rstrip())
file.close()

print("\n* Sorting lines in a list:")
with open("pythonPrac.txt") as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
file.close()
"""

