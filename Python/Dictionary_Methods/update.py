# Adding new key-value pairs
profile = {"name": "Eyob", "age": 22}
new_info = {"city": "Addis Ababa", "occupation": "Student"}

profile.update(new_info) 
print(profile) # Output: {'name': 'Eyob', 'age': 22, 'city': 'Addis Ababa', 'occupation': 'Student'}

# Updating an existing value
settings = {"color": "blue", "theme": "dark"}
changes = {"color": "red"}

settings.update(changes)
print(settings) # Output: {'color': 'red', 'theme': 'dark'}

# Using keyword arguments
user = {"id": 1, "status": "active"}
user.update(email="alice@example.com", points=100)
print(user) # Output: {'id': 1, 'status': 'active', 'email': 'alice@example.com', 'points': 100}