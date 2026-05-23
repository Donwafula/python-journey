# Program stores a secret number.
# Ask user to guess. If guess is correct, print "Correct!" Otherwise, print "Wrong guess"
# Add hints: Too high, Too low

secret_number = 7

try:
    guess = int(input("Guess the correct number: "))
except ValueError:
    print("Invalid input")
else:
    if guess == secret_number:
        print("Correct")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")
