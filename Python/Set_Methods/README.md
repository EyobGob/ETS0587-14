# add() Method
The add() method in Python is used to add a specified element to a set. If the element is already present in the set, the set remains unchanged (as sets do not allow duplicate elements).

Adds a Single Element: You can only add one element at a time using add().
No Duplicates: If you try to add an element that already exists in the set, nothing happens. The set will not contain multiple instances of the same element.
Modifies the Set In-Place: The add() method directly alters the original set. It doesn't return a new set.
Immutable Elements: You can only add immutable elements (like numbers, strings, and tuples) to a set. Trying to add mutable elements (like lists or dictionaries) will result in a TypeError.

# update() Method
The update() method in Python is used to add multiple elements to a set from an iterable (such as another set, list, tuple, or string). For each element in the iterable, if it's not already present in the set, it will be added. Duplicate elements from the iterable are ignored, and the original set is modified in-place.

# remove() Method
The remove() method in Python attempts to remove a specified element from a set. If the element is found within the set, it is removed. However, if the element is not present in the set, the remove() method will raise a KeyError, halting the program if not handled with error handling mechanisms (like a try-except block).