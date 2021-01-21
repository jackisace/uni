from modules import *


def notes(mainHistory):
    history = mainHistory
    while True:
        clear("")
        print("Notes")
        print("=====")
        print("history: \n" + history)
        print("\nEnter your notes below, enter q on its own to quit when you are done:\n")
        line = raw_input("")
        if "quit" in line:
            return history
        if "help" in line:
            Help("Notes")

        line = spell(line)
        line = word(line)

        history += line + "\n"



