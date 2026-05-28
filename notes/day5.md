# Functions

Are reusable blocks of code that perform specific tasks\
_Basic structure of a function:_
```
def function_name():
    # code_block
    pass
```

__Simple function:__\
```
def say_hello():
    print("Hello, student!")

say_hello()
```

__Function with input(parameters):__\
Functions can receive data.
```
def greet(name):
    print(f"Hello {name}")

greet("Alice")
greet("Brian")
```
Output:
```
Hello Alice
Hello Brian
```
`name` is a _parameter_

__Multiple parameters__\
```
def add(a, b):
    print(a + b)

add(5, 3)
```
Output: `8`

__Return values__\
```
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

- Print shows output whereas return gives value back
- Print ends communication whereas return gives a reusable result
- Print is used for display whereas return is used for computation

_Functions:_\
1. Keep code structure clean
2. Provides reusable logic
3. Makes debugging easier

__Functions in Data Science__\
_Functions in DS are used for:_\
1. Cleaning data
2. Transforming columns
3. Calculating statistics
4. Preprocessing datasets

__Scope__\
Variable inside functions are normal:
```
def test():
    x = 10
    print(x)

test()
```
But outside: `print(x)  #ERROR`