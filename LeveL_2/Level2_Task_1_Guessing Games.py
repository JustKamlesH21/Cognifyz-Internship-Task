#Guessing Game
import random
numbeer = random.randint(1, 100)
print(numbeer)  # For debugging purposes, you can remove this line later
attempts = 0
print("Welcome to the Guessing Game!")
print("I have selected a number between 1 and 100.")
while True:
    guess = input("Please enter your guess: ")
    if not guess.isdigit():
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    attempts+= 1
    guess = int(guess)
    
    if guess < 1 or guess > 100:
        print("Your guess is out of range. Please try again.")
    elif guess < numbeer:
        print("Too low! Try again.")
    elif guess > numbeer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break