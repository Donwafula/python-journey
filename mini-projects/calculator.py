# Simple calculator mini-project
# asks for two numbers and performs addition, subtraction, multiplication and division on them
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
if num2 != 0:
    print(f"Division: {num1 / num2:.2f}")
else:
    print("Error: Division by zero is not allowed.")