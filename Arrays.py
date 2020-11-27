# For loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print()



for x in range(2, 30, 3):
    print(x, end = " ")
print()



print()
for x in range(7):
    print(x, end = " ")
else:
    print("Finally finished!")
print()




# Add 10 to argument a, and return the result
x = lambda a : a + 10
print(x(5))
print()




#  function that always doubles the number you send in
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
print()
print()






# 2D arrays/lists

# First method to create a 1D array
N = 5
arr = [0] * N
print("First method to create a 1D array:", arr) # 1A


# Second method to create a 1 D array
N = 5
arr = [0 for i in range(N)]
print("Second method to create a 1 D array:", arr) # 1B
print()


# 2D ARRAYS
# First method to create a 2D Array
rows, cols = (3,3)
arr = [[0] * cols] * rows
print("First method to create a 2D Array:\n", arr) # 2A
print()


# Second method to create a 2D array
rows, cols = (3,3)
arr = [[1 for i in range(cols)] for j in range(rows)]
print("Second method to create a 2D Array:\n", arr) # 2B
print()


# Third method to create a 2D array
rows, cols = (3, 3)
arr = []
for i in range(cols):
    col = []
    for j in range (rows):
        col.append(2)
    arr.append(col)
print("Third method to create a 2D array:\n", arr)
print()


# 2A with first element changed to 1
rows, cols = (3, 3)
arr = [[0] * cols] * rows
# below change the first element of the first row to 1
arr[0][0] = 1

for rows in arr:
    print("Notice the first element is 1:\n", rows) # 2A with first element changed to 1
# outputs the following
#[1, 0, 0]
#[1, 0, 0]
#[1, 0, 0]
print()



# Change the second element of the first row to 2
ver, hor = [3, 4]
arr = [[0 for i in range(ver)] for j in range(hor)]
# below change the second element of the first row to 2
arr[0][1] = 2
for hor in arr:
    print(hor)
print()

