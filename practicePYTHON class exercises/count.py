
number = int(input("Enter a number between 1 and 10: "))
import random   
number = random.randint(1, 10)
while True:
    guess = int(input("Guess the number: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        break