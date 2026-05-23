# Loops
Allows a program to repeat actons, process large data sets, automate tasks, avoid rewriting code

__`for` loop__\
Repeats through a sequence\
Example:
```
for number in range(5):
  print(number)
```
Output:
```
0
1
2
3
4
```

`range(5)` doesn't include 5. Starts at 0 and ends at 4\
`range(1, 6)` will start at 1 and end at 5

_repeating text:_
```
for i in range(3):
  print("Python is fun)
```
Output:
```
Python is fun
Python is fun
Python is fun
```

__`while` loop__\
Repeats while a condition stays _true_
Example:
```
count = 1

while count <= 5:
  print(count)
  count += 1  #if this statement misses or is incorrect, an _infinite loop_ is created
```

__`break` statement__\
Immediately stops a loop
```
for number in range(10):
  if number == 5:
    break
    
  print(number)
```
Output:
```
0
1
2
3
4
```
Loop stops at 5.

__`continue` statement__\
Skips one iteration
```
for number in range(5):
  if number == 2:
    continue
  print(number)
```
Output:
```
0
1
3
4
```
2 is skipped

__Nested loops__\
A loop inside another loop\
Example:
```
for i in range(3):
  for j in range(2):
    print(i, j)
```
Output:
```
0, 0
0, 1
1, 0
1, 1
2, 0
2, 1
```
Important for: matrices, tables, machine learning


# Lists