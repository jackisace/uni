from modules import *

def main():
    historyFile = open("history.txt", "r")
    history = historyFile.read()
    historyFile.close
    msg = ""
    while True:
        clear(msg)
        msg = ""
        print("Main Menu")
        print("=========")
        print("\n\n1) Workbook")
        print("2) Theasaurus")
        print("3) Spell checker")
        print("4) Classes")
        print("5) Games")
        print("6) Notes")
        print("7) Calculator")
        print("8) Maths Test")
        ui = input("\n").lower()[0]
        if "q" in ui:
            historyFile = open("history.txt", "w")
            historyFile.write(history)
            historyFile.close
            quit()
        elif "h" in ui:
            Help("Main Menu")
        elif "1" in ui:
            history = workbook(history)
        elif "2" in ui:
            history = thesaurus(history)
        elif "3" in ui:
            history = spellChecker(history)
        elif "4" in ui:
            classes()
        elif "5" in ui:
            games()
        elif "6" in ui:
            history = notes(history)
        elif "7" in ui:
            history = calc(history)
        elif "8" in ui:
            mathsTest()
        else:
            msg = "I'm sorry, I didn't get that?"
            continue

if __name__ == "__main__":
    main()

