# implementing the game High and Low. 
# The computer chooses a random integer between 1 and 100 and
# lets the user guess the value. After each guess, 
# the user is given a clue of the type higher or lower.

import random


def guessGame():
    
    guess = 0
    start = 1
    end = 100
    number_to_guess = random.randint(start, end)
    
    while True:
        userNumber = int(input("Guess a number between 1 to 100: "))
        guess += 1
        if userNumber == number_to_guess:
            print(f'Great you guessed right!! {userNumber} in {guess} attempts')
            break
        elif userNumber < number_to_guess:
            print('Guess a higher number')
        else:
            print('Guess a lower number!')
        
guessGame()