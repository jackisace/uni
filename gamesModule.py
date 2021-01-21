from modules import *


def games():
    msg = ""
    while True:
        clear(msg)
        msg = ""
        print("Games")
        print("=====")
        print("\n1) Hangman")
        print("2) Higher or lower")
        print("3) Riddle of the day")
        print("4) Number guess")
        print("\nhelp) Ask at any time for help")
        print("quit) Quit program")
        ui = raw_input("\nEnter your selection :")[0]
        if "q" in ui:
            return
        elif "h" in ui:
            Help("Games")
        elif "1" in ui:
            hangman()
        elif "2" in ui:
            highLow()
        elif "3" in ui:
            riddle()
        elif "4" in ui:
            numberGuess()
