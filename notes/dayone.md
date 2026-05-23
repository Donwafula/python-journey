# variables; input/output; math; data types

Created my first python program _hello.py_ to print my name:\
```
print("My name is Donald")
```

__Comments:__ #
```
# Python program to print my name
print("My name is Donald")
```

__Variables__\
They are used to store information\
e.g.:
```
name = "Donald"
age = 10
height = 1.5
```
_Rules:_ start with lowercase letters, no spaces, use _ instead of -,

_Printing variables:_\
e.g.:
```
# Python program to print my detaols
name = "Donald"
age = 10
height = 1.5

print(name)
print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I am {height} meters tall")

```
Output:
```
Donald
My name is Donald
"I am 10 years old
I am 1.5 meters tall
```

__Data types__\
  string - text\
  integer - whole number\
  float - decimal numbers\
  boolean - true or false\

use `type()` to check data types

__Math operators__\
a + b:  addition\
a - b:  subtraction\
a * b:  multiplication\
a / b:  true division\
a // b: floor division. Rounds down to nearest whole number\
a % b:  modulus (int remainder)\
a ** b: exponential (a raised to power b)\
-a:     negation

__Input__\
programs can ask questions\
e.g.:
```
name = input("What is your name? ")
```
`input()` always gives text\
in `age = input("Enter age: ")`, age becomes a string.\
if you want numbers:
```
age = int(input("Enter age))
weight = float(input("Enter weight: "))
```