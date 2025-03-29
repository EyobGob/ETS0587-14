my_list = ["apple", "banana", "cherry"]
result1 = ", ".join(my_list)
print(result1)  # Output: apple, banana, cherry

my_tuple = ("one", "two", "three")
result2 = "-".join(my_tuple)
print(result2)  # Output: one-two-three

my_set = {"A", "B", "C"}
result3 = "".join(my_set)
print(result3) # Output: ABC (the order of the set elements is random or not indexed)