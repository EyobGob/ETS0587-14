# Using integers
set_a = {1, 2, 3}
set_b = {4, 5, 6}
set_c = {3, 7, 8}

print(f"Is set_a disjoint from set_b? {set_a.isdisjoint(set_b)}") # Output Is set_a disjoint from set_b? True
print(f"Is set_a disjoint from set_c? {set_a.isdisjoint(set_c)}") # Output Is set_a disjoint from set_c? False

# Using string
basket_one = {"apple", "banana", "orange"}
basket_two = {"grape", "watermelon", "kiwi"}
basket_three = {"banana", "mango", "pineapple"}

print(f"Are basket_one and basket_two disjoint? {basket_one.isdisjoint(basket_two)}") # Output Are basket_one and basket_two disjoint? True
print(f"Are basket_one and basket_three disjoint? {basket_one.isdisjoint(basket_three)}") # Output Are basket_one and basket_three disjoint? False


