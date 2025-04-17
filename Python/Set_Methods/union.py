# Create two sets of numbers
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Set 1: {set1}") # Output: Set 1: {1, 2, 3}
print(f"Set 2: {set2}") # Output: Set 2: {3, 4, 5}

# using the union() method
union_set_method = set1.union(set2)
print(f"Union using union() method: {union_set_method}") # Output: Union using union() method: {1, 2, 3, 4, 5}

# using the | operator
union_set_operator = set1 | set2
print(f"Union using | operator: {union_set_operator}") # Output: Union using | operator: {1, 2, 3, 4, 5}   

# Create a set and a list
my_set = {10, 20}
my_list = [20, 30, 40]
print(f"\nMy Set: {my_set}") # Output: My Set: {10, 20}
print(f"My List: {my_list}") # Output: My List: [20, 30, 40]

# Union of the set and the list
union_set_mixed = my_set.union(my_list)
print(f"Union of set and list: {union_set_mixed}") # Output: Union of set and list: {40, 10, 20, 30}  

# Create a set and a string
my_set_chars = {'a', 'b'}
my_string = "bcd"
print(f"\nMy Set (chars): {my_set_chars}") # Output: My Set (chars): {'a', 'b'}
print(f"My String: {my_string}") # Output: My String: bcd

# Union of the set and the string
union_set_string = my_set_chars.union(my_string) 
print(f"Union of set and string: {union_set_string}") # Output: Union of set and string: {'d', 'a', 'b', 'c'}