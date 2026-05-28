# Asks user for a number and prints multiplication from 1 to 12
# Example 7 x 1 = 7
# If user enters invalid number, print "Invalid number" and prompt them to enter a number again until they enter a valid number

while True:
    try:
        num = int(input("Enter number: "))
        break
    except ValueError:
        print("Invalid number")

for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")
