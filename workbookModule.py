from modules import *


def workbook(mainHistory):
    history = mainHistory
    msg = ""
    while True:
        clear(msg)
        msg = ""
        print("history: \n" + history)
        print("Workbook")
        print("========")
        try:
            ui = raw_input("\nEnter calculations (ie. 7*3) or just write notes :)\n\n")
        except IndexError:
            continue
        if "quit" == ui:
            return history
        if "q" == ui:
            return history
        if "h" == ui:
            Help("Workbook")
            continue
        if "help" == ui:
            Help("Workbook")
            continue
        isCalc = True
        for char in ui:
            if char.isalpha():
                isCalc = False
        if isCalc:
            if "+" in ui:
                a = float(ui.split("+")[0])
                b = float(ui.split("+")[1])
                c = a+b
                st = "{}+{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
            elif "-" in ui:
                a = float(ui.split("-")[0])
                b = float(ui.split("-")[1])
                c = a-b
                st = "{}+{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
            elif "*" in ui:
                a = float(ui.split("*")[0])
                b = float(ui.split("*")[1])
                c = a*b
                st = "{}+{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
            elif "/" in ui:
                a = float(ui.split("/")[0])
                b = float(ui.split("/")[1])
                c = a/b
                st = "{}+{}={}\n".format(a, b, c)
                st = st.replace(".0", "")
                history += st
                print(st)
        else:
            ui = spell(ui)
            ui = word(ui)
            history += ui + "\n"

        historyLines = history.count("\n")
        while historyLines > 19:
            found = history.find("\n", 2)
            history = history[found:]
            historyLines = history.count("\n")
            



