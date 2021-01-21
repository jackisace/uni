from modules import *

def highLow():
    score = 0
    while True:
        number = random.randint(0,100)
        nextNumber = random.randint(0,100)
        clear("")
        print("quit) quit to main menu\n")
        answer = raw_input("The number is {}, will the next one be higher or lower?: ".format(number))[0]
        if "q" in answer:
            return
        if "help" in answer:
            Help("Higher or Lower")
            continue
        if "h" in answer:
            if number < nextNumber:
                score += 1
                if score == 3:
                    print("Well done, you have won!")
                else:
                    print("Well done! you have got {} in a row, get 3 to win".format(score))
            else:
                score = 0
                print("Unlucky, keep trying!")
        if "l" in answer:
            if number > nextNumber:
                score += 1
                if score == 3:
                    print("Well done, you have won!")
                else:
                    print("Well done! you have got {} in a row, get 3 to win".format(score))
            else:
                score = 0
                print("Unlucky, keep trying!")
        raw_input("Press Enter to continue")
        if score == 3:
            return

        



