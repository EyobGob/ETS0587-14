original_dict = {'name': 'Eyob', 'age': 22}
copied_dict = original_dict.copy()

print(f"Original dictionary: {original_dict}") # Output: Original dictionary: {'name': 'Eyob', 'age': 22}
print(f"Copied dictionary: {copied_dict}") # Output: Copied dictionary: {'name': 'Eyob', 'age': 22}

# Modify the copied dictionary
copied_dict['name'] = 'Abel'
copied_dict['age'] = 18
copied_dict['city'] = 'Addis Ababa'
 
print(f"Original dictionary: {original_dict}") # Output: Original dictionary: {'name': 'Eyob', 'age': 22}
print(f"Copied dictionary: {copied_dict}") # Output: Copied dictionary: {'name': 'Abel', 'age': 18, 'city': 'Addis Ababa'}


