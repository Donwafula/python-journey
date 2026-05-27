# Ask user to enter 5 numbers
# Store them in a list
# Print: all numbers, largest, smallest, average

numbers = []
index = 1

while index < 6:
    try:
        entry = int(input(f"Enter number {index}: "))
        numbers.append(entry)

    except ValueError:
        print("Invalid input")
        continue
    index += 1
print(f"All numbers; {numbers}")
print(f"Largest: {max(numbers)}\nSmallest: {min(numbers)}\nAverage: {(sum(numbers))/(len(numbers)):.2f}")
