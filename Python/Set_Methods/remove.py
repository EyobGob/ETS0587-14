my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

my_set.remove(5)
print(my_set)  # Output: {1, 2, 4}

# Trying to remove an element that doesn't exist will raise a KeyError:
# my_set.remove(6)  # Raises KeyError: 6

# Using try-except to handle potential KeyError:
try:
    my_set.remove(6)
except KeyError:
    print("The element 6 was not found in the set.")
print(my_set)  # Output: {1, 2, 4} (the set remains unchanged)