keys = ['name', 'age', 'city']

default_value = "unknown"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict) # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

keys = "abc"
initial_count = 0
new_dict = dict.fromkeys(keys, initial_count)
print(new_dict) # Output: {'a': 0, 'b': 0, 'c': 0}

