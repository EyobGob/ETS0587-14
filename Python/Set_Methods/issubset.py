# Using Integers
set_a = {1, 2}
set_b = {0, 1, 2, 3}

is_a_subset_of_b = set_a.issubset(set_b)
print(is_a_subset_of_b) # Output: True

# Both Integer and String
set_c = {"5", "6"}
set_d = {"banana", "apple"}

is_c_subset_of_d = set_c.issubset(set_d)
print(is_c_subset_of_d) # Output: False

empty_set = set()
another_set = {5, 10}

is_empty_subset = empty_set.issubset(another_set)
print(is_empty_subset) # Output: True

# Using Strings
math_club = {"Eyob", "Rediet", "Yohannes"}
science_club = {"Earmiyas", "Leul", "Amaha", "Nati"}

is_math_subset_of_science = math_club.issubset(science_club)
print(is_math_subset_of_science) # Output: False

is_science_subset_of_math = science_club.issubset(math_club)
print(is_science_subset_of_math) # Output: False

programming_club = {"Eyob", "Rediet"}
is_programming_subset_of_math = programming_club.issubset(math_club)
print(is_programming_subset_of_math) # Output: True

