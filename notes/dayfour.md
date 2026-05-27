# Lists
A list stores multiple values of the same variable
Example: a list of scores
```
scores = [80, 75, 90, 60]
```
Instead of:
```
score1 = 80
score2 = 75
...
```
Lists are the foundations of understanding:
1. NumPy arrays
2. Pandas columns
3. datasets
4. machine learning data

__Creating lists__\
Number list: `numbers = [1, 2, 3, 4, 5]`\
String list: `names = ["Alice", "Brian", "Cynthia"]`\
Mixed list: `data = ["Donald", 10, True, 1.5]`

__Accessing list items__\
_index:_ item position in a list\
Example: `fruits = ["apple", "banana", "mango"]`\
index 0 = apple\
index 1 = banana\
index 2 = mango\
Access example:\
`print(fruits[0])`\
Output:\
`apple`\
__Important:__ Python indexing starts at 0 NOT 1

__Negative indexing__\
You can count from the end:\
`print(fruits[-1])`\
Output:
`mango`\
index -1 = last item\
index -2 = second last item

__Changing list values__
Lists are mutable.\
Example:
```
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)
```
Output:\
`['apple', 'orange', 'mango']`

__Adding items__\
`append()`: adds items to the end of the list.
```
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```
Output: `[1, 2, 3, 4]`\

__Removing items__\
`remove()`
```
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)
```
Output: `['apple', 'mango']`

__List length__\
Use `len()`\
```
numbers = [1, 2, 3, 4]
print(len(numbers))
```
Output: `4`

__Looping through lists__
```
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```
Output:
```
apple
banana
mango
```

__Working with numbers in lists__
```
scores = [80, 90, 70, 60]
total = 0

for score in scores:
    total += score

print(total)
```
Output: `300`

__Finding average__
```
scores = [80, 90, 70, 60]
total = 0

for score in scores:
    total += score

average = total / len(scores)

print(f"Average {avearge}")
```

`len()` - count items\
`max()` - largest value\
`min()` - smallest value\
`sum()` - total

__Sorting lists__
```
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)
```
Output: `[1, 2, 5, 8]`

__Reverse sorting__\
`numbers.sort(reverse=True)`

__List slicing__\
Extract part of a list.\
```
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])
```
Output: `[2, 3, 4]`
_Slice rules:_\
`[start:end]`
- start included
- end excluded

__`zip()`__\
Pairs items from multiple lists:
```
names = ["Alice", "Brian", "Cynthia"]
scores = [90, 75, 82]
combined = zip(names, scores)

print(list(combined))
```
Output: `[('Alice', 90), ('Brian', 75), ('Cynthia', 82)]`
_Used for:_
1. merging related colums
2. paring labels with values
3. combining data sets
4. synchronized iterations
__`zip()` stops at the shortest list__


__`lambda`__\
Is a quick temporary funtion\
_normal function:_
```
def square(x):
    return x * x
```
_usage:_ `print(square(5))`\
_Output:_ `25`\

_same thing using lambda:_\
```
square = lambda x: x * x
print(square(5))
```
_same output:_ `25`\

__Structure of lambda__\
`lambda parameter: result`\
Example: `lambda x: x + 1`\
Means: _take x and return x + 1_

`lambda` mostly used for:
1. sorting
2. quick transformations
3. small temporary operations
4. filtering datasets
5. applying calculations


__`enumerate()`__\
Get index + Value together\
Normally:
```
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```
You get values only.
With `enumerate()`:
```
fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
Output:
```
0 apple
1 banana
2 mango
```
Without it:
```
for i in range(len(fruits)):
    print(i, fruits[i])
```

`enumerate()` helps with:
1. row numbering
2. indexing data
3. tracking iterations
debugging loops