"""code to the following cell to swap variables a and b(so that
a refers to the object previously referred to by b and vice versa)."""

a = [1, 2, 3]
b = [3, 2, 1]

# solution
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")