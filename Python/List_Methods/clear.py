my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}") # Output: Original list: [1, 2, 3, 4, 5]
print(f"Length of original list: {len(my_list)}") # Output: Length of original list: 5  

my_list.clear() 
print(f"List after clear(): {my_list}") # Output: List after clear(): []
print(f"Length of list after clear(): {len(my_list)}") # Output: Length of list after clear(): 0

another_list = ['a', 'b', 'c']
print(f"Before clear(): {another_list}") # Output: Before clear(): ['a', 'b', 'c']
another_list.clear()
print(f"After clear(): {another_list}") # Output: After clear(): []