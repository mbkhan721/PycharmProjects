""" Muhammad Khan
Exercise 2: Write a program that prompts the user
for their name. When they respond, write their
name to a file called “guest.txt”. """
name = input("Enter your name: ")
fout = open("pythonPrac.txt", "a")
fout.write(name)
fout.close()
print("Value assigned")
