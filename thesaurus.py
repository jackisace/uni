from modules import *

def thesaurus(mainHistory):
    history = mainHistory
    while True:
        clear("")
        print("Thesaurus")
        print("=========")
        print("history: \n" + history)
        print("\nEnter your notes below, enter q on its own to quit when you are done:\n")
        ui = raw_input("")
        if "quit" == ui:
            return history
        if "q" == ui:
            return history
        if "h" == ui:
            Help("Thesaurus")
            continue
        if "help" == ui:
            Help("Thesaurus")
            continue

        ui = word(ui)

        history += ui + "\n"

