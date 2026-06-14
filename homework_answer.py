# Ask the user to enter numbers until they type 0.
# Keep track of the total sum.

total = 0
number = int(input("Enter a number (0 to stop): "))

while number != 0:
    total = total + number
    print(total)
    number = int(input("Enter a number (0 to stop): "))

print("Total = " + str(total))


