my_dict = {"name": "Eyob", "age": 22, "city": "Addis Ababa"}

# Key exists
name = my_dict.get("name")
print(f"Name: {name}")  # Output: Name: Alice

age = my_dict.get("age")
print(f"Age: {age}")    # Output: Age: 30

# Key does not exist, no default provided (returns None)
country = my_dict.get("country")
print(f"Country: {country}")  # Output: Country: None


