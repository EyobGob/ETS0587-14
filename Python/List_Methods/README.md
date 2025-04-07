# append()
The append() method in Python is a fundamental list method used to add a single element to the end of a list. 
The primary purpose of append() is to modify a list in-place by adding a new element at the very end.
It increases the length of the list by one.

# extend()
In Python, the extend() method is a powerful and efficient way to add multiple elements to the end of a list. It modifies the original list in place, meaning it doesn't create a new list.
The primary purpose of extend() is to append all the items from an iterable (like another list, tuple, string, set, or dictionary's keys) to the end of an existing list.
The extend() method iterates through each item in the iterable and appends each individual item to the end of list1. This is different from the append() method, which adds the entire iterable as a single element to the end of the list.

# insert()
In Python, the insert() method is a built-in list method that allows you to add an element to a list at a specific index. Unlike append(), which always adds elements to the end of the list, insert() provides precise control over where the new element is placed.
The primary purpose of insert() is to insert a given element into a list at a specified index. All the elements originally at and after that index are shifted one position to the right to accommodate the new element.

# remove()
The remove() method is a built-in function in Python that is primarily used with lists. It allows you to remove the first occurrence of a specified value from the list.
Modifies the list in-place: The remove() method directly alters the original list. It does not return a new list with the element removed.
Removes by value: You need to provide the specific value you want to remove as an argument to the remove() method. You do not specify the index.
Removes the first occurrence: If the list contains multiple instances of the specified value, only the first one encountered (from left to right) will be removed. 

# pop()
The pop() method is a built-in function in Python specifically designed for lists. It provides a way to remove and return an element from the list at a specified index.
Modifies the list in-place: Like remove(), pop() directly alters the original list by removing the element.
Removes by index: Unlike remove() which removes by value, pop() requires an index as an argument to specify which element to remove.
Returns the removed element: This is a crucial difference from remove(). pop() returns the value of the element that was removed from the list. This allows you to use the removed element immediately.
Removes the last element if no index is provided: If you call pop() without any arguments, it defaults to removing and returning the last element of the list (similar to how a stack operates).

# clear()
The clear() method is a built-in function in Python specifically designed for lists. Its sole purpose is to remove all elements from the list, effectively making it an empty list.
Modifies the list in-place: The clear() method directly alters the original list. It does not return a new empty list.
No arguments: The clear() method does not take any arguments.
Result is an empty list: After calling clear() on a list, the list will have a length of 0 and contain no elements.
No return value (returns None implicitly): The clear() method does not explicitly return any value. In Python, functions that don't have a return statement implicitly return None.
