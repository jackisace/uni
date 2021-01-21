from modules import *
operators = ["+", "-"]

def mathsTest():
    correct = 0
    helpPrep("You are in Maths Test")

    for i in range(0,10):
        operator = random.randint(0,1)
        operator = operators[operator]
        answer = -1
        if operator == "+":
            a = random.randint(0,10)
            b = random.randint(0,10)
            answer = a+b
        if operator == "-":
            while answer < 0:
                a = random.randint(0,10)
                b = random.randint(0,10)
                answer = a-b
            
        print("\nquit) to quit to main menu\n")
        valid = False
        while not valid:
            user = raw_input("What is {}{}{}?: ".format(a,operator,b))
            if "q" in user:
                return
            try:
                user = int(user)
                valid = True
            except ValueError:
                valid = False
        if user == answer:
            clear("Well done!")
            correct += 1
        else:
            clear("Unlucky! The answer was {}".format(answer))


    if correct == 5 and correct == 6:
        raw_input("\n\nYou got {}/10, well done!".format(correct))
    elif correct == 7 and correct == 8:
        raw_input("\n\nYou got {}/10, really well done!".format(correct))
    elif correct == 9:
        raw_input("\n\nYou got {}/10, Great work!".format(correct))
    elif correct == 10:
        raw_input("\n\nYou got {}/10, Amazing!!".format(correct))
    else:
        raw_input("\n\nYou got {}/10 ".format(correct))



    


