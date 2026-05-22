# Program that creates a student profile with name, age, and favorite subject and height
# Program should ask the user for these details
# Print a profile like this:
"""
--- STUDENT PROFILE ---
Name: Donald
Age: 10
Favorite Subject: Science
Height: 1.5 meters
"""
# Get user input for name, age, favorite subject, and height
name = input("What is your name? ")
age = int(input("What is your age? "))
favorite_subject = input("What is your favorite subject? ")
height = float(input("What is your height in meters? "))

# Print the student profile
print("--- STUDENT PROFILE ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Subject: {favorite_subject}")
print(f"Height: {height} meters")