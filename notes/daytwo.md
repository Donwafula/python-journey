# Conditional logic

__The `if` staement__\
Used to make decisions\
e.g:
```
age = 20
if age >= 18:
  print("You are an adult")
```
Meaning: __IF__ the condition is `true` (age is greater that 18),  run the indented code. `if false`, skip the code

__Comparison operators__\
`==`: Equal to
`!=`: Not equal to
`>` : Greater than
`<` : Less than
`>=`: Greater than or equal to
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
Here, python skips the `print("Adult")` line