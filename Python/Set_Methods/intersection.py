# Intersection of Integers
set_a = {1, 2, 3, 4, 5}
set_b = {3, 5, 6, 7}
set_c = {5, 8, 9}

# Find elements common to set_a and set_b
common_ab = set_a.intersection(set_b)
print(f"Intersection of set_a and set_b: {common_ab}")  # Output: Intersection of set_a and set_b: {3, 5}

# Find elements common to set_a, set_b, and set_c
common_abc = set_a.intersection(set_b, set_c)
print(f"Intersection of set_a, set_b, and set_c: {common_abc}")  # Output: Intersection of set_a, set_b, and set_c: {5}

set_d = {10, 11}
# Intersection with a set that has no common elements
common_ad = set_a.intersection(set_d)
print(f"Intersection of set_a and set_d: {common_ad}")  # Output: Intersection of set_a and set_d: set() (an empty set)

# Intersection of strings
group_a_fruits = {"Apples", "Bananas", "Oranges"}
group_b_fruits = {"Bananas", "Grapes", "Oranges"}

common_fruits = group_a_fruits.intersection(group_b_fruits)

print(f"Fruits liked by both groups: {common_fruits}") # Output: Fruits liked by both groups: {'Oranges', 'Bananas'}