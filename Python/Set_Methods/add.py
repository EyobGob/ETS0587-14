my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}

my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.add(2)  # Adding an existing element
print(my_set)  # Output: {1, 2, 3, 4} (no change)

my_set.add("hello")
print(my_set)  # Output: {1, 2, 3, 4, 'hello'}

