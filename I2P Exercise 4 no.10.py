import string


def is_pangram(sntc):
    for i in string.ascii_lowercase:
        if i not in sntc.lower():
            return False
    return True


if __name__ == "__main__":
    sentence = input("Please add a sentence:")
    if is_pangram(sentence) is True:
        print("sentence is a pangram")
    else:
        print("Not a pangram")
