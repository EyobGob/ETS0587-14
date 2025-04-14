my_info = {"name": "Eyob", "age": 22}
print(f"Original info: {my_info}") # Output: Original info: {'name': 'Eyob', 'age': 22}

# Check for an existing key
city = my_info.setdefault("city", "Addis Ababa")
print(f"value of city: {city}") # Output: value of city: Addis Ababa
print(f"Info after checking city: {my_info}") # Output: Info after checking city: {'name': 'Eyob', 'age': 22, 'city': 'Addis Ababa'}

# Check for a non-existent key and set a default value
occupation = my_info.setdefault("occupation", "Engineer")
print(f"value of occupatoin: {occupation}") # Output: value of occupatoin: Engineer
print(f"Info after setting occupation: {my_info}") 
# Output: Info after setting occupation: {'name': 'Eyob', 'age': 22, 'city': 'Addis Ababa', 'occupation': 'Engineer'}
