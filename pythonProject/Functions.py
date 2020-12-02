# star* means unlimited args
def my_function(*kids):
    #for name in kids:
        #print(name)
    #print(kids)
    print("The youngest child is " + kids[4])
my_function("Emil", "Tobias", "Linus", "John", "Khan")

print()
print("------------- Exercise 12 -------------")
print()

import random
from random import randrange
n = 10
a = [randrange(1, 7) for i in range(n)]
print("Roll of dice this time is:", a)

print()
print("------------- Exercise 13 -------------")
print()

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print("The sum of all number is:", sum((1, 2, 3, 4, 5)))

print()
print("------------- Exercise 14 -------------")
print()

def smFact(n):
    if (n % 2 == 0):
        return 2;

    i = 3;
    while(i * i <= n):
        if (n % i == 0):
            return i;
        i += 2;
    return n;

n = 81; # Enter a number here to find its smallest factor

print("Smallest factorial of the given number is: ", smFact(n));

print()
print("------------- Exercise 15 -------------")
print()

def Reverse_int(val):
    rev = 0
    while val > 0:
        digit = val % 10
        rev = (rev*10) + digit
        val = val//10
    return rev

#val = int(input("Enter upto 10 numbers to reverse: "))
rev = Reverse_int(123)
print("Reversed numbers are: %d" %rev)
print()


"""
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False
   
if is_divisible(10, 2):
    print("yes")
else:
    print("no")
    

def printHello():
    print("Hello")
#end function
# main
printHello()

pi = 3.14159
def circleArea(radius):
    area = pi * radius * radius
    return area
#end function
# main  
ans = circleArea(1) # add 2 or 3 or any number
print(ans)


import random

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.randrange(0, 101, 2))

def dice ():
    return random.randrange(1, 7)

for i in range(10):
    ans = dice()
    print (ans, end = " ")


def factorial(val):
    res = 1
    while val > 1:
        res *= val
        print(val, res)
        val -= 1
    print()
ans = factorial(4)

def displayReverse(val):
    while val > 0:
        digit = val % 10
        print (digit, end = " ")
        val = val//10
        
#end while
# end of function
        
displayReverse(123)
birthday = "05/20/1986"
print(birthday)
print()

mylist = birthday.split("/")
print(mylist)
print()

def num_year(birthdaylist):
    birthyear = int(birthdaylist[2])

    targetyear = 2020

    yearsalive = targetyear - birthyear
    return yearsalive
print("I am", num_year(mylist),"years old")
print()

student1 = {
    'Name': 'Khan',
    'ET574': 'B',
    'ET710': 'A',
}

student2 = {
    'Name': 'Azeem',
    'ET574': 'A',
    'ET710': 'C',
}


student1["age"] = 34
student2["age"] = 2

studentlist = [student1, student2]
studentlist = []
studentlist.append(student1)
studentlist.append(student2)
print(studentlist)
print()

for dict in studentlist:
    print("Name:", dict["Name"], "Age:", dict["age"])
    print( "\tET574:", dict["ET574"] )
    print( "\tET710:", dict["ET710"] )
    print()


def my_function(fname):
    print(fname + " Khan")
my_function("Muhammad")
my_function("Fatima")
my_function("Azeem")

print()

def my_list(*kids):
  print("The youngest cild is " + kids[2])
my_list("Fatima", "Refsnes", "Azeem")

print()

def my_count(country = "Pakistan"):
  print("I am from " + country)

my_count("Sweden")
my_count("India")
my_count()
my_count()
my_count("Brazil")

print()

def my_kitchen(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_kitchen(fruits)

print()

def my_multi(x):
  return 5 * x

print(my_multi(3))
print(my_multi(5))
print(my_multi(9))

print()

def myexample():
    pass
"""
