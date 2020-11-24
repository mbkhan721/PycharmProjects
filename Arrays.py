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

