my_dict = {"apple": 1, "banana": 2, "orange": 3}
print(f"Original dictionary: {my_dict}") # Output: Original dictionary: {'apple': 1, 'banana': 2, 'orange': 3}

removed_item = my_dict.popitem()
print(f"Removed item: {removed_item}") # Output: Removed item: ('orange', 3)
print(f"Dictionary after popitem(): {my_dict}") # Output: Dictionary after popitem(): {'apple': 1, 'banana': 2}