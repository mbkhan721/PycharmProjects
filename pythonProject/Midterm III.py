"""  Muhammad Khan -- Midterm III
You are to write a program that prints weekly sales for an employee using
a 2 dimensional array (list of lists).  Name this array list2Dsales. Note that
the program should work correctly for any number of items and you should put
relevant comments in your code."""
import random
# 1.	Create a string containing your first name, middle initial and last name
name = "Muhammad B. Khan"
print("My name is:", name)

# 2.	Remove all blanks and punctuation marks
myName = name.replace(" ", "")
myName = myName.replace(".", "")

# 3.	Convert to upper case
myName = myName.upper()
print("MyName =", myName)

# Adding the ASCII values of all the letters in the name
seed = 0
for letters in myName:
    value = ord(letters)
    seed += value
print("My seed =", seed)
random.seed(seed)
print()
# 4.	Limit the quantities between 0 and 5.  Limit the prices to 9 dollars.
# 5.	Create and print a list (listItems) for 6 items sold.
# each item should be 5 characters long

# Filled some list items with blanks to make it 5 chars
listItems = ["Pencil", "Pen  ", "Book ", "Backpack", "Eraser", "Glue "]
listItems = ["Pencil", "Pen  ", "Book ", "Backpack",]

# 6.	Create and print a list (listDays) for the five days of the week (Mon-Fri)
listDays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# 7.	Create a function itemSoldPerDay that generates and returns a list of random
# integers between 0 and 9 where each integer represents the number of each item sold per day.
vertical = len(listItems)
horizontal = len(listDays)
