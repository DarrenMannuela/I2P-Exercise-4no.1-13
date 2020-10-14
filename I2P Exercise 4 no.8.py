words = ["Hi", "Hello", "Filo", "Rapthalia", "Mercy"]

def _longest_word(lwords):
    numbers = []
    for word in range(len(lwords)):
        character = len(lwords[word])
        numbers.append(character)

    long_words = max(numbers)

    return numbers, long_words


if __name__ == "__main__":
    print(_longest_word(words))
