# Create list of first foods
# Print first food, last food
# Add another food
# Remove one food
# Print final list

foods = ["meat", "veges", "omena", "beans", "maize"]
print(foods)
print(f"First food: {foods[0]}\nLast food: {foods[-1]}")

foods.append("githeri")
print(foods)
foods.remove(foods[1])
print(foods)
print(len(foods))
