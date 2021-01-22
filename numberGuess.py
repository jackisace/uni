from modules import *

def numberGuess():
    number = random.randint(0,100)
    guessed = False
    guesses = 0
    while not guessed:
        user = input("Guess your number between 0 and 100: ")
        if "help" in user:
            if Help("Number Guess") == 1:
                return 1
        guesses += 1
        if user < number:
            print("Higher")
        elif user > number:
            print("Lower")
        elif user == number:
            print("Congratulations! you got it right in {} guesses".format(guesses))
            input("")
            guessed = True
    return


