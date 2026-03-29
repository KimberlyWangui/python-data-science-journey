import random

value = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess < value:
    print("Too low! Try again.")       
elif guess > value:
    print("Too high! Try again.")
else:
    print("Correct! You've guessed the number!")