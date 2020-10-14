words = ["Hi", "Hello", "Filo", "Rapthalia", "Mercy"]

def words_to_digits(lst):
    numbers = []
    for word in range(len(lst)):
        character = len(lst[word])
        numbers.append(character)
    return numbers


if __name__ == "__main__":
    print(words_to_digits(words))
