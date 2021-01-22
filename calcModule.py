from modules import *


def calc(mainHistory):
    history = mainHistory
    msg = ""
    while True:
        clear(msg)
        msg = ""
        print("history: \n" + history)
        print("Calculator")
        print("==========")
        try:
            ui = input("\nEnter calculations (ie. 7*3)\n\n")
        except IndexError:
            continue
        if "quit" == ui:
            return history
        if "q" == ui:
            return history
        if "h" == ui:
            if Help("Calculator") == 1:
                return history
        if "help" == ui:
            if Help("Calculator") == 1:
                return history
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

        historyLines = history.count("\n")
        while historyLines > 19:
            found = history.find("\n", 2)
            history = history[found:]
            historyLines = history.count("\n")
            



