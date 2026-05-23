# Checks if a number is is positive, negetive or zero
# First check if the input is a number, if not print "Invalid input"
try:
    num = float(input("Enter number: "))
except ValueError:
    print("Invalid input!")
else:
    if num == 0:
        print("Zero")
    elif num > 0:
        print("Positive")
    else:
        print("Negative")
