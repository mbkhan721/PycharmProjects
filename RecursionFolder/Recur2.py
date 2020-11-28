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
