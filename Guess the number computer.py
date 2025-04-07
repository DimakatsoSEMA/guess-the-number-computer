#Guess the number computer 
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 

    while guess != random_number: ##WHILE GUESS IS NOT EQUAL THE NUMBER #While Loop 
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print('sorry your number is TOO LOW, guess again')
        elif guess > random_number:
            print('your number is TOO HIGH, guess again')
        
    print(f'You did it! the number is {guess}')

guess(10)
