def makeforming(verb):
    if verb[-1] == "e":
        verb = verb[0:-1]
        verb = verb + "ing"
    elif verb[-2:] == "ie":
        verb = verb[0:-1] + "y" + "ing"
    elif verb[-2] == "a":
        verb = verb[0:-1] + verb[-1] + verb[-1] + "ing"
    elif verb[-2] == "i":
        verb = verb[0:-1] + verb[-1] + verb[-1] + "ing"
    elif verb[-2] == "u":
        verb = verb[0:-1] + verb[-1] + verb[-1] + "ing"
    elif verb[-2] == "e":
        verb = verb[0:-1] + verb[-1] + verb[-1] + "ing"
    elif verb[-2] == "o":
        verb = verb[0:-1] + verb[-1] + verb[-1] + "ing"
    else:
        verb = verb + "ing"

    return verb


if __name__ == "__main__":
    word = input("Please input a verb:")
    print(makeforming(word))
