# Using String
fruits = ('apple', 'banana', 'apple', 'orange', 'apple', 'grape')

position_of_banana = fruits.index('banana')
print(f"The first 'banana' is at index: {position_of_banana}") # Output: The first 'banana' is at index: 1

position_of_orange = fruits.index('orange')
print(f"The first 'orange' is at index: {position_of_orange}") # Output: The first 'orange' is at index: 3

# Using Integer
numbers = (10, 25, 5, 30, 15, 25)

index_of_25 = numbers.index(25)
print(f"The first number 25 is at index: {index_of_25}") # Output: The first number 25 is at index: 1

index_of_10 = numbers.index(10)
print(f"The number 10 is at index: {index_of_10}") # Output: The number 10 is at index: 0

# Let's try to find a number that's not in the tuple
# This will raise a ValueError:
index_of_42 = numbers.index(42)
print(f"The number 42 is at index: {index_of_42}") # Output: Error (ValueError: tuple.index(x): x not in tuple)
