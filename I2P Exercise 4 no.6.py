def histogram(lst):
    lst = list(lst)
    for i in range(len(lst)):
        print("*"*lst[i])


if __name__ == "__main__":
    data = eval(input("input data:"))
    histogram(data)