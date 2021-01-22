from modules import *


def notes(mainHistory):
    history = mainHistory
    while True:
        clear("")
        print("Notes")
        print("=====")
        print("history: \n" + history)
        print("\nEnter your notes below, enter q on its own to quit when you are done:\n")
        line = input("")
        if line == "q":
            return history
        if line == "help":
            if Help("Notes") == 1:
                return history
        if "quit" in line:
            return history
        if "help" in line:
            if Help("Notes") == 1:
                return history

        line = spell(line)
        line = word(line)

        history += line + "\n"



