from clear import *



def word(line):
    library = [["building", "structure", "architecture", "home", "house", "hut"], ["animal", "beast", "creature", "pet"]]
    if line == "q":
        return history

    finder = line.split(" ")
    for item in library:
        found = False
        for libraryWord in item:
            if found:
                break
            for lineWord in line.split(" "):
                if found:
                    break
                if libraryWord in lineWord:
                    answer = raw_input("By {}, did you mean any of these? \n{} \ny/n: ".format(lineWord, item))
                    if "y" in answer:
                        library.remove(item)
                        line += " ("
                        for word in item:
                            line += word + " "
                        line = line[:len(line)-1] +  ")"
                        found = True

    return line



