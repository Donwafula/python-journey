# variables; input/output; math; data types

Created my first python program hello.py to print my name:
print("My name is Donald")

Comments: #

Variables - store information
e.g.:   name = "Donald"
        age = 10
        height = 1.5

Rules: start with lowercase letters, no spaces, use _ instead of -,

Printing variables:
e.g.:   print(name)
        print("My name is", name)
        print("I am", age, "years old")

Data types
    string - text
    integer - whole number
    float - decimal numbers
    boolean - true or false

    use type() to check data types

Math operators
    a + b:  addition
    a - b:  subtraction
    a * b:  multiplication
    a / b:  true division
    a // b: floor division. Rounds down to nearest whole number
    a % b:  modulus (int remainder)
    a ** b: exponential (a raised to power b)
    -a:     negation

Input
programs can ask questions
e.g.: name = input("What is your name? ")
input() always gives text
    age = input("Enter age: ")
    age becomes a string.
if you want numbers:
    age = int(input("Enter age))
    weight = float(input("Enter weight: "))