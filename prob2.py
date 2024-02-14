
string_list = ["apple", "banana", "kiwi", "orange", "grape", "pear"]
sorted_list = sorted(string_list, key=lambda x: (len(x), x))
print(sorted_list)
