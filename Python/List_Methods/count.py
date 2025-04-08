my_list = [10, 20, 30, 20, 40, 20]

count_of_20 = my_list.count(20) # Count the occurrences of 20
print(f"The number 20 appears {count_of_20} times.")  # Output: The number 20 appears 3 times.

count_of_10 = my_list.count(10) # Count the occurrences of 10
print(f"The number 10 appears {count_of_10} time.")   # Output: The number 10 appears 1 time.

count_of_50 = my_list.count(50) # Count the occurrences of a value that doesn't exist
print(f"The number 50 appears {count_of_50} times.")   # Output: The number 50 appears 0 times.

# Count occurrences in a list with different data types
mixed_list = [1, "hello", 2.5, "hello", True, 1]

count_of_hello = mixed_list.count("hello")
print(f"'hello' appears {count_of_hello} times.")     # Output: 'hello' appears 2 times.

count_of_1 = mixed_list.count(1)  # True is considered equal to 1 in count
print(f"The number 1 appears {count_of_1} times.")       # Output: The number 1 appears 3 times.

count_of_true = mixed_list.count(True)
print(f"The boolean True appears {count_of_true} times.") # Output: The boolean True appears 3 times.