def multiplication_table():
    table_size = int(input("State the size of the multiplication table:"))
    for column in range(0, table_size+1):
        print("")
        for row in range(0, table_size+1):
            print(row*column, end=" ")


multiplication_table()
