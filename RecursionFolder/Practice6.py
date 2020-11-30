""" Muhammad Khan

1. Write a program that recursively counts down from n.
a) Create a recursive function named countdown that accepts an
integer n, and progressively decrements and outputs the value of n.
b) Test your function with a few values for n."""

def countdown(n): # def recursive_function(parameters)
    if n <= 0:    # countdown stops at 1 since the parameter is 0
        return n  # return base_case_value
    else:
        print(n)
        countdown(n - 1) # countdown decrements by 1
countdown(5)
print()



""" 2. Write a function called numEven that returns the number of even
digits in a positive integer parameter.
For example, a program that uses the function numEven follows.
print(numEven(23)) # prints 1
print(numEven(1212)) # prints 2
print(numEven(777)) # prints 0 """

def numEven(n): # defining numEven Function
    even_count = 0  # making initial count=0

    while (n > 0): #  checking input number greater than 0 or not
        rem = n % 10 #slashing up inputted number into digits
        if (rem % 2 == 0): #verifing digit is even or odd by dividing with 2.if remainder=0 then digit is even
            even_count += 1 #counting the even digits
        n = int(n / 10)
    print(even_count) #printing the even number count
    if (even_count % 2 == 0): #exits the function
        return 1
    else:
        return 0
numEven(23)
numEven(1212)
numEven(777)
print()



""" 3. Write a function called lastEven that returns the last even digit
in a positive integer parameter. It should return 0 if there are no
even digits.
For example, a program that uses the function lastEven follows.
print(lastEven(23)) # prints 2
print(lastEven(1214)) # prints 4
print(lastEven(777)) # prints 0 """

def lastEven(x):
    if x == 0:
        return 0
    remainder = x % 10
    if remainder % 2 == 1:
        return lastEven(x // 10)
    if remainder % 2 == 0:
        return remainder + lastEven(x // 10)

print(lastEven(23))
print(lastEven(1212))
print(lastEven(777))
print()


