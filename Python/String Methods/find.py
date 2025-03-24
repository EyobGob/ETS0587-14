text = "Hello, Python is awesome!"

index = text.find("Python") # Searching for 'Python'
print(index)  # Output: 7 (index where 'Python' starts)

not_found = text.find("Java") # Searching for a substring not present
print(not_found)  # Output: -1

index_in_range = text.find("is", 8, 16) # Specifying a range for the search
print(index_in_range)  # Output: 14
