def overlapping(lst1, lst2):
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst2.count(lst1[i]) <= 1:
                return True
            else:
                return False


if __name__ == "__main__":
    index01 = list(input("List01:"))
    index02 = list(input("List02:"))
    print(overlapping(index01, index02))
