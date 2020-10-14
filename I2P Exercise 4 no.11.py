import string


def char_freq(text):
    txt = text.lower()
    for i in string.ascii_lowercase:
        if txt.count(i) == 0:
            pass
        else:
            print(i, ":", txt.count(i))


if __name__ == "__main__":
    word = input("Please give a word:")
    print(char_freq(word))