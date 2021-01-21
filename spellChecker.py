from modules import *

def spellChecker(mainHistory):
    history = mainHistory
    while True:
        clear("")
        print("Spell Checker")
        print("=============")
        print("history: \n" + history)
        print("\nEnter your notes below, enter q on its own to quit when you are done:\n")
        line = raw_input("")
        if line == "help":
            Help("Spell checker")
            continue
        if line == "h":
            Help("Spell checker")
            continue
        if line == "quit":
            return history
        if line == "q":
            return history

        line = spell(line)

        history += line + "\n"

