from modules import *

allClasses = ["Art", "Science", "Maths", "English", "History", "Drama", "Music", "PE", "Cooking", "IT"]

def classes():
    classesFile = open("classes.txt", "rw")
    currentClasses = classesFile.read().split("\n")
    classesFile.close()
    classesFile = None
    while True:
        clear("")
        print("Classes")
        print("=======")
        print("\n\nYour classes for today are: ")
        for eachClass in currentClasses:
            print(eachClass)
        print("update) update your classes")
        print("quit) main menu")
        user = raw_input("\n")[0]
        if "h" in user:
            Help("Classes")
        if "q" in user:
            return
        if "u" in user:
            print("Classes")
            print("=======")
            print("\n\nYour classes for today are: ")
            i = 0
            clear("")
            for eachClass in currentClasses:
                if i < len(currentClasses) - 1:
                    i += 1
                    print("{}) {}".format(i, eachClass))
            userA = input("please select which one you need to update: ") - 1 

            j = 0
            clear("")
            for eachAllclass in allClasses:
                if j < len(allClasses) - 1:
                    j += 1
                    print("{}) {}".format(j, eachAllclass))
            userB = input("please select which one you need to update to: ") - 1

            currentClasses[userA] = allClasses[userB]

            i = 1
            classesFile = open("classes.txt", "w")
            for eachClass in currentClasses:
                if i < len(currentClasses) - 1:
                    classesFile.write(eachClass)
                    classesFile.write("\n")
            classesFile.close()
            classesFile = None




