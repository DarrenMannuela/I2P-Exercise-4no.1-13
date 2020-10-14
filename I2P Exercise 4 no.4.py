def is_member(val, a):
    if a.count(val) <= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    value = input("Give any value:")
    storage = list(input("Give me a list"))
    print(is_member(value, storage))
