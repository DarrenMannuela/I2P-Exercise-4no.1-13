
sample_list = []

sample_data = str(input("sample data:"))
print(sample_data)
for i in range(0, len(sample_data), 2):
    sample_list.append(sample_data[i])

sample_tuple = tuple(sample_list)

print("Output:")

print("List:", sample_list)
print("Tuple:", sample_tuple)
