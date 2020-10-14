
def makeforms(verb):
    if verb[-1] == "y":
        verb = verb[0:-1]
        verb = verb + "ies"
    elif verb[-1] == "o":
        verb = verb + "es"
    elif verb[-1] == "s":
        verb = verb + "es"
    elif verb[-1] == "x":
        verb = verb + "es"
    elif verb[-1] == "z":
        verb = verb + "es"
    elif verb[-2:] == "ch":
        verb = verb + "es"
    elif verb[-2:] == "sh":
        verb = verb + "es"
    else:
        verb = verb + "s"
    return verb


if __name__ == "__main__":
    word = input("Please input a verb:")
    print(makeforms(word))
