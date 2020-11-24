# Muhammad Khan
# A class is like a "blueprint" for creating objects

# To create a class, use the keyword class
class MyClass:
    x = 5
print(MyClass)

# use the class named MyClass to create objects
obj = MyClass() # Create an object named obj
print(obj.x) # print the value of x
print()


"""All classes have a function called __init__(),
which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties,
"""

class Person:    # Create a class named Person
    def __init__(self, name, age):  # use the __init__() function to assign values for name and age
        self.name = name
        self.age = age

person1 = Person("John", 36)
print(person1.name)
print(person1.age)
print()

# The __init__() function is called automatically every time the class is being used to create a new object.

# OBJECT METHODS
# Methods in objects are functions that belong to the object.

# create a method in the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)

person1 = Person("Muhammad", 34)
person1.myfunc()
print()

"""The self parameter is a reference to the current instance of the class
and is used to access variables that belong to the class.
It doesn't have to be named self, but it has to be the first parameter of any function in the class """

class Azeem:
    def __init__(mykid, name, age, place):
        mykid.name = name
        mykid.age = age
        mykid.place = place

    def mychild(khan):
        print("My child name is " + khan.name,", she is", khan.age,". She lives in", khan.place)

ch1 = Azeem("Fatima", 4, "New York")
ch1.mychild()
print()


# You can modify properties on objects
# Lets modify the age property
ch1.age = 2
print(ch1.age)
print()

# To delete the age property: del person1.age
# To delete the person1 object: del person1
