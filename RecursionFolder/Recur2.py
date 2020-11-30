def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

countdown(5)
print()

#spacer = "-> "
def count(spacer, n):
    spacer = "--" + spacer
    if n < 1:
        print(spacer, "Blastoff!")
    else:
        print(spacer, n)
        count(spacer, n-1)

count(">", 10)
print()



def remove_first(n):
    digit = n % 10
    print("N =", n, "Digit =", digit)

    if n < 10:
        print("Base case")
        return 0

    ret = remove_first(n//10)
    val = digit + 10 * ret
    print("Return =", ret, "Value =", val)
    return val
print(remove_first(1234))

# print(18 // 4)  called Floor Division outputs 4
# // Quotient when a is divided by b, rounded to the next smallest whole number

# print(18 % 4) called modulus outputs 2
