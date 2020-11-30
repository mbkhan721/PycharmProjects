# Muhammad Khan
n = 8
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = "="
        elif i > j:
            a[i][j] = "*"
        else:
            a[i][j] = "-"
for row in a:
    print('= '.join([str(elem) for elem in row]))
print()




y = 8
z = [["X"] * y for k in range(y)]
for k in range(y):
    for b in range(y):
        if k < b:
            z[k][b] = 0
        else:
            z[k][j] = "X"
    print(([str(elem) for elem in row]))



# To process 2-dimensional array, you typically use nested loops

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):  # The first loop iterates through the row number
    for j in range(len(a[i])):  # the second loop runs through the elements inside of a row
        print(a[i][j], end=' ')
print()
print()



a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
print()
print()



"""
Naturally, to output a single line you can use method join():
for row in a:
 print(' '.join([str(elem) for elem in row]))
 """
b = [[7, 2, 1], [4, 5, 6], [6]]
for row in b:
    print(' '.join([str(elem) for elem in row]), end = " ")
print()
print()


# This is how you can use 2 nested loops to calculate the sum of all the numbers in the 2-dimensional list
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print("The sum of all numbers in this list is:", s)
print()

# Or the same with iterating by elements, not by the variables i and j
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for row in a:
    for elem in row:
        s += elem
print("Easier way to add the sum of all numbers in 2D list.\n", s)
print()


""" First, note that elements that lie above the main diagonal – are elements a[i][j] for which i<j, and
that for elements below the main diagonal i>j. Thus, we can compare the values i and j, which determines 
the value of a[i][j]. We get the following algorithm: """

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))
print()



n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
        a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))
print()


n = 4
a = [0] * n
for i in range(n):
    a[i] = [2] * i + [1] + [0] * (n - i - 1)
for row in a:
    print(' '.join([str(elem) for elem in row]))
print()


n = 4
a = [0] * n
a = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
for row in a:
    print(' '.join([str(elem) for elem in row]))
print("----------------- Line 129 -------------------------")
print()

n = 8
a = [["*"] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = "="
        #a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = "*"
for row in a:
    print(' '.join([str(elem) for elem in row]))
print()



# print(18 // 4)  called Floor Division outputs 4
# // Quotient when a is divided by b, rounded to the next smallest whole number

# print(18 % 4) called modulus outputs 2



"""2. Display the American flag using a nested loop of these dimensions:
 20x7 flag
 7x4 stars as *
 Alternate = and – to represent stripe colors

*******=============
*******-------------
*******=============
*******-------------
====================
--------------------
====================
"""

for i in range(1, 8):   # Loops through rows 1 to 7
    for j in range(1, 29):  # Loops through columns 1 to 20
        if j <= 10 and i <=4:    # Check for the stars
            print("*", end="")  # Prints the stars
        elif i % 2 == 0:    # Checks for alternate lines
            print("-", end="")  # Prints dash
        else:
            print("=", end="")  # Prints equals
    print()
