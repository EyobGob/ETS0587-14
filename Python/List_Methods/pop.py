my_list = ['apple', 'banana', 'cherry', 'date']
print(f"Original list: {my_list}") # Output: Original list: ['apple', 'banana', 'cherry', 'date']

removed_item1 = my_list.pop(1) # Remove and return the element at index 1 ('banana')
print(my_list) # Output: ['apple', 'cherry', 'date']

removed_item2 = my_list.pop() # Remove and return the last element ('date')
print(my_list) # Output: ['apple', 'cherry']
