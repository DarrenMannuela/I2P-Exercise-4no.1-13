words = ["Hi", "Hello", "Filo", "Rapthalia", "Mercy"]


def _longest_words(lwords, char):
    numbers = []
    updated_list = []
    for word in range(len(lwords)):
        character = len(lwords[word])
        numbers.append(character)

    for limit in range(len(numbers)):
        if numbers[limit] > char:
            updated_list.append(lwords[limit])
        else:
            continue

    return numbers, updated_list


if __name__ == "__main__":
    min_char = int(input("Minimal amount of character:"))
    print(_longest_words(words, min_char))