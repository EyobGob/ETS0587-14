my_list = [10, 20, 30, 20, 40]

index_of_20 = my_list.index(20)
print(f"Index of the first 20: {index_of_20}")  # Output: Index of the first 20: 1

index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")      # Output: Index of 30: 2

index_of_20_from_2 = my_list.index(20, 2) # Search for 20 starting from index 2
print(f"Index of 20 starting from index 2: {index_of_20_from_2}")  # Output: Index of 20 starting from index 2: 3

