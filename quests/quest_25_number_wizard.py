import random

number_to_guess = random.randint(1, 20)
guess = None

while guess != number_to_guess:
    user_input = input("Guess a number between 1 and 20: ")
    
    if not user_input.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(user_input)
    
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
