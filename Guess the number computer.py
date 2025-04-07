#Guess the number computer 
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    attempts = 0  # Track the number of tries

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        attempts += 1  # Increase the count with each guess

        if guess < random_number:
            print('Too LOW, try again.')
        elif guess > random_number:
            print('Too HIGH, try again.')

    print(f'You got it! The number was {guess}.')
    print(f'It took you {attempts} attempts.')

guess(10)
