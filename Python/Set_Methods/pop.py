# Create a set of colors
colors = {"red", "green", "blue"}
print(f"Initial set: {colors}") # Output: Initial set: {'red', 'green', 'blue'}


popped_color = colors.pop() # Pop an element from the set
print(f"Popped color: {popped_color}") # Output: Popped color: red
print(f"Set after pop(): {colors}") # Output: Set after pop(): {'green', 'blue'}


another_popped_color = colors.pop() # Pop another element
print(f"Popped color again: {another_popped_color}") # Output: Popped color again: green
print(f"Set after second pop(): {colors}") # Output: Set after second pop(): {'blue'} 


empty_set = set() # Create an empty set
print(f"\nInitial empty set: {empty_set}")  # Output: Initial empty set: set()

# Trying to pop from an empty set will raise a KeyError
try:
    popped_from_empty = empty_set.pop()
    print(f"Popped from empty set: {popped_from_empty}")  # This line won't be reached
except KeyError as e:
    print(f"Error: {e}") 