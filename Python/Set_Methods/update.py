my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}

another_set = {3, 4, 5} # Adding elements from another set
my_set.update(another_set)
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_list = [5, 6, 7, 2] # Adding elements from a list
my_set.update(my_list)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7} (the duplicate '2' is ignored)

my_string = "hello" # Adding characters from a string
my_set.update(my_string)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 'h', 'e', 'l', 'o'} (order may vary)