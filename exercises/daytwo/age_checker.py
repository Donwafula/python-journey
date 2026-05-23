# Program to check for age of the user
# If under 13, print "child". 13 - 19, print "Teenager". 20+, print "Adult"

age = int(input("Enter your age: "))

if age >= 20:
    print("Adult")
elif age >=13:
    print("Teenager")
else:
    print("Child")
