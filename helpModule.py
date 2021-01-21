from modules import *


def Help(strIn):
    global helpMsg
    clear("")
    print("Help")
    print("====\n")
    print("You are currently in " + strIn)
    print("\nhelp) Ask at any time for help")
    print("quit) Quit program")
    print("main) Main menu")
    print("continue) Continue with the program")
    user = raw_input("\nEnter your selection")
    if "h" in user:
        Help(strIn)
    if "q" in user:
        quit()
    if "c" in user:
        return
    if "m" in user:
        main()

