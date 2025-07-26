import random
#Number Guesser
def number_guesser():
    print("Welcome to the Number Guessing Game!")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    number = random.randint(lower, upper)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between {lower} and {upper}: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

number_guesser()