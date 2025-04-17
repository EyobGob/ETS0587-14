my_set = {1, 2, 3, 4, 5}

my_set.discard(3)
print(my_set)  # Output: {1, 2, 4, 5}

my_set.discard(6)  # 6 is not in the set, no error is raised
print(my_set)  # Output: {1, 2, 4, 5}

my_set.remove(2)
print(my_set)  # Output: {1, 4, 5}

# my_set.remove(6)  # This would raise a KeyError

fruits = {"apple", "banana", "mango"}
print(f"Initial set: {fruits}") # Output: Initial set: {'mango', 'banana', 'apple'}

fruits.discard("banana")
print(f"After discarding 'banana': {fruits}") # Output: After discarding 'banana': {'mango', 'apple'}

fruits.discard("orange")
print(f"After discarding 'orange': {fruits}") # Output: After discarding 'orange': {'mango', 'apple'}
