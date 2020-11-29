def month_days(month, days):
    result = f"{month} has {days} days."
    return (result)
print(month_days("June", 30))
print(month_days("July", 31))
print()

def numEven(n): #defining numEven Function

    even_count = 0 #making initial count=0

    while (n > 0): #checking input number greater than 0 or not
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
#numEven(int(input("Enter to find out even numbers: "))) #inputing number
print()

"""
print("Number 2:", numEven(23))
print("Number 2:", numEven(1212))
print("Number 2:", numEven(777))
print()
"""
