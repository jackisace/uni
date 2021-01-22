from modules import *
from clear import *
from hangman import *
from highLow import *
from riddle import *
from helpModule import *
from numberGuess import *


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
        ui = input("\nEnter your selection :")[0]
        if "q" in ui:
            return
        elif "h" in ui:
            if Help("Games") == 1:
                return
        elif "1" in ui:
            if hangman() == 1:
                return
        elif "2" in ui:
            if highLow() == 1:
                return
        elif "3" in ui:
            if riddle() == 1:
                return
        elif "4" in ui:
            if numberGuess() == 1:
                return
