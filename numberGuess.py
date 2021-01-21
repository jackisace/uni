from modules import *

def numberGuess():
    user = input("How high do you dare to go?: ")
    number = random.randint(0,user)
    guessed = False
    guesses = 0
    while not guessed:
        user = input("Guess your number: ")
        if "help" in user:
            Help("Number Guess")
        guesses += 1
        if user < number:
            print("Higher")
        elif user > number:
            print("Lower")
        elif user == number:
            print("Congratulations! you got it right in {} guesses".format(guesses))
            raw_input("")
            guessed = True
    return


