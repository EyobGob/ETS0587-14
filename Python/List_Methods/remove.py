my_list = [1, 2, 3, 2, 4, 2]
print(f"Original list: {my_list}") # Output: Original list: [1, 2, 3, 2, 4, 2]

my_list.remove(2)  # Removes the first occurrence of 2
print(my_list) # Output: [1, 3, 2, 4, 2]

my_list.remove(4)
print(my_list) # Output: [1, 3, 2, 2]   

