my_list = [3, 1, 4, 1, 5, 9, 2, 6]

my_list.sort() # Sort in ascending order (default)
print(f"Sorted list: {my_list}")  # Output: Sorted list: [1, 1, 2, 3, 4, 5, 6, 9]

my_list.sort(reverse=True) # Sort in descending order
print(f"Sorted list: {my_list}") # Output: Sorted list: [9, 6, 5, 4, 3, 2, 1, 1]

another_list = ["banana", "apple", "cherry", "date"]

another_list.sort() # Sort strings alphabetically (ascending)
print(f"Sorted list: {another_list}")  # Output: Sorted list: ['apple', 'banana', 'cherry', 'date']

another_list.sort(reverse=True) # Sort strings in reverse alphabetical order
print(f"Sorted list: {another_list}") # Output: Sorted list: ['date', 'cherry', 'banana', 'apple']

