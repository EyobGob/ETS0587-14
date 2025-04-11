# clear()
The clear() method is a fundamental built-in method for Python dictionaries. Its purpose is straightforward: it removes all items (key-value pairs) from the dictionary, leaving it empty.
When you call clear() on a dictionary object, it iterates through all the key-value pairs within that dictionary and deletes them.
After the operation is complete, the dictionary object still exists in memory, but it contains no elements. Its length becomes 0.

# copy()
The copy() method in Python dictionaries is used to create a shallow copy of the dictionary. This means it creates a new dictionary object with a new memory address, but the items within the dictionary are references to the original items.
copy() creates a new dictionary object.
The new dictionary contains the same keys and values as the original dictionary.
For immutable values (like integers, floats, strings, tuples), the new dictionary will contain independent copies of these values.
For mutable values (like lists, other dictionaries, sets), the new dictionary will contain references to the same objects as the original dictionary. Changes made to these mutable objects through either the original or the copied dictionary will affect both.

# fromkeys()
The fromkeys() method is a built-in dictionary method in Python that allows you to create a new dictionary with specified keys and an optional common value for all of them.
The primary purpose of fromkeys() is to efficiently initialize a dictionary where you know the keys in advance, and you want to assign the same initial value to all of them. If you don't provide a value, it defaults to None.

# get() Method
The get() method is a fundamental and often preferred way to access values from a dictionary in Python. It provides a safer and more flexible alternative to using square bracket notation ([]).
The primary purpose of the get() method is to retrieve the value associated with a specified key in a dictionary. However, unlike the square bracket notation, get() allows you to handle cases where the key might not exist in the dictionary without raising a KeyError.

# items() Method
The items() method in Python dictionaries is used to retrieve a view object that displays a list of a dictionary's key-value tuple pairs. This view object is dynamic, meaning that if the dictionary changes, the view object will reflect those changes.
The primary purpose of items() is to provide an efficient way to iterate over both the keys and their corresponding values in a dictionary simultaneously. This is particularly useful when you need to perform operations that involve both the key and the value of each item in the dictionary.