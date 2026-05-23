# Conditional logic

__The `if` statement__\
Used to make decisions\
e.g:
```
age = 20
if age >= 18:
  print("You are an adult")
```
Meaning: __IF__ the condition is `true` (age is greater that 18),  run the indented code. `if false`, skip the code

__Comparison operators__\
`==`: Equal to\
`!=`: Not equal to\
`>` : Greater than\
`<` : Less than\
`>=`: Greater than or equal to\
`<=`: Less than or equal to

__Important:__`=` is an assignment operator\
`age = 10` means assign the value 10 to age or store 10 in age

Example 2: Password check:
```
password = input("Enter password: ")
if password == "@Python123":
  print("Access granted")
```
Output:
```
Acess granted
```
Take note of indentation\
Wrong:
```
if password == "@Python123":
print("Access granted")
```

__The `else` statement__\
Runs when the condition is false\
Example:
```
age = 15

if age >= 18:
  print("Adult")
else:
  print("Minor")
```
Output:
```
Minor
```
Here, python __skips__ the `print("Adult")` line and __runs__ the `print("Minor")` line

__The `elif` statement__\
Used where we need many conditions to be checked.\
Example:
```
score = 75

if score >= 80:
  print("Grade A")
elif score >= 70:
  print("Grade B")
elif score >= 60:
  print("Grade C")
else:
  print("Fail")
```
Output:
```
Grade B
```
__NOTE:__ Python checks from top to bottom and stops at the first true condition

__Logical operators__\
`and`: Both must be true\
`or` : at least one must be true\
`not`: reverses the condition\

Example - `and`:
```
age = 20
has_id = True

if age >= 18 and has_id:
  print("Entry allowed")
```
Example - `or`:
```
day = "Sunday"

if day == "Saturday" or day == "Sunday":
  print("Weekend")
```
Example - `not`:
```
is_raining = False

if not is_raining:
  print("Go outside")
```