# Program stores a secret number.
# Ask user to guess. If guess is correct, print "Correct!" Otherwise, print "Wrong guess"
# Add hints: Too high, Too low
# Improved game: keep asking untill correct guess

import random

secret_number = random.randint(1, 20)
attempts = 0

while True:
    while True:
        try:
            guess = int(input("Guess the correct number: "))
            break
        except ValueError:
            print("Invalid input")
    
    attempts += 1
    if guess == secret_number:
        print(f"Correct! Attempts: {attempts}")
        break
    elif guess > secret_number:
        print(f"Attempt {attempts}\nToo high\n")
    else:
        print(f"Attempt {attempts}\nToo low\n")
