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
#       each item should be 5 characters long
#n = 6
# n = 4
#       Filled some list items with blanks to make it 5 chars
listItems = ["Pencl", "Blpen  ", "Book ", "Bakpak", "Erasr", "Glue "]
#listItems = ["Pencl", "Blpen  ", "Book ", "Bakpak",]
n = len(listItems)
# 6.	Create and print a list (listDays) for the five days of the week (Mon-Fri)
listDays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
print("Days = 5", listDays)
print("Items", n, listItems)

# 7.	Create a function itemSoldPerDay that generates and returns a list of random
#       integers between 0 and 9 where each integer represents the number of each item sold per day.
def itemSoldPerDay(n):
    lst = []
    for i in range(n):
      lst.append(random.randint(0, 9)) # Producing random int from 0 -- 9
    return lst
while True:
    if len(listItems) > n:
        del listItems[-1]
    else:
        break
# each integer that represents the number of each item sold per day
price = []
for p in range(n):
    # Limiting price to 9 dollars.
    # 9.	Create a list of random prices for each item between 1.00 and 10.00
    #       (rounded to 2 decimal places) and print the list.
    price.append(round(random.uniform(1.00, 10.00), 2)) # List of random prices
print("List of prices = ", price) # Outputs the prices rows
print()

# 8.	Create a blank 2D array for sales (list2Dsales). The rows are the days and
#       the columns are the items. Use itemsSoldPerDay and listDays to fill this array

table=[]
for i in range(n):
    table.append(itemSoldPerDay(n))
print('\t', '\t', '\t', "Weekly sales for:", name)
print('\t', '\t', '\t', "**********************************\n")
print("Item", end = "\t")
for item in listItems:
    print(item, end = "\t")
print("Totals")
print("Price ", end = "\t")
for item in price:
    print(item, end = "  \t ")
print()
print("        ------  ------  -----   ------  ------  -----  --------")

# 10.	Create a function rowTot that will multiply the price of each item by
#       the quantity rounded to 2 decimal places and print the result
def rowTot(row, price):
    i = 0
    s = 0
    for i in range(len(row)):
        s = s + row[i] * price[i]
    return round(s, 2) #round of values to 2 decimal pts

# 11.	Create a function colTot which will print the total items in each column.
def colTot(table, n): # Finding total number item sold in a week
    piece = []
    for k in range(n):
        piece.append(0)
    for i in range(0, n):
        m = 0
        for row in table:
            piece[i] = piece[i] + row[i]
            m += 1
            if m == n - 1:
                break;
    return piece

# 12.	Create a function colAmt which will multiply the price of each item by the
#       daily quantity,  round to 2 decimal places and print the result
def calAmt(piece,price): #calculating Total in column wise
    Total = []
    for i in range(len(piece)):
        Total.append(round(piece[i] * price[i], 2))
    return Total

j=0
for day in listDays: # Printing 2D array
    if j==n:
        break
    print(day, end = '\t')
    row=table[j]

# Number of items sold on a daily basis
    for item in row:
        print("     ", item, end = '\t')
    total=rowTot(row,price)
    print("   $", total)
    j += 1
print("        ------  ------  -----   ------  ------  -----")
print('Pieces', end = '\t')
pieces = colTot(table, n)

# The total number of pieces sold weekly
for item in pieces:
    print(" ", item, end = "\t")
print()
print('Total',end='\t')
Total=calAmt(pieces,price)

# Printing the total weekly sale
for item in Total:
    print(item, end = "\t")
print()
