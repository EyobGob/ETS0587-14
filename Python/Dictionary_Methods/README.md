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

# keys() Method
The keys() method in Python is a built-in function that returns a view object displaying a list of all the keys in a dictionary. This view object dynamically reflects any changes made to the dictionary. It's important to note that in Python 3.7 and later, this view object maintains the insertion order of the keys.

# pop() Method
The pop() method in Python removes and returns the value associated with a specified key from a dictionary. If the key is not found, it raises a KeyError 1  unless a default value is provided as a second argument. In that case, if the key is not found, the default value is returned, and the dictionary remains unchanged.

# popitem() Method
Imagine you have a box of random things (a dictionary!). The popitem() method is like reaching into the box without looking and grabbing whatever you happen to touch.

In Python, when we call popitem() on a dictionary, it does two things:
i. Removes a key-value pair: It picks an arbitrary (meaning you can't predict which one) key-value pair from the dictionary and takes it out.
ii. Returns the removed pair: It gives you back the key and the value it just removed as a tuple (like a little package of two things).

# setdefault()
The setdefault() dictionary method in Python lets us to:
i. Check if a key exists: we give it a key. If that key is already in our dictionary, it just returns the corresponding value that's already there – like looking up something in our notebook and reading what we've already written.

ii. Add a key with a default value if it doesn't exist: If the key you provide is not in the dictionary, it will add that key to the dictionary along with a value that we also provide (the "default" value). It then returns this new value – like adding a new entry to our notebook with a specific initial piece of information.

# update() Method
In essence, the update() method allows us to merge the contents of one dictionary into another. Think of it as a way to efficiently add new key-value pairs or modify existing ones in our target dictionary.

When we call update() on a dictionary (let's call it dict1), and provide another dictionary (let's call it dict2) as an argument, Python does the following:
i. Adds new key-value pairs: If a key in dict2 does not exist in dict1, that key-value pair from dict2 is added to dict1.
ii. Updates existing values: If a key in dict2 does already exist in dict1, the value associated with that key in dict1 is overwritten with the value from dict2.

# values() Method
The values() method is a straightforward way to retrieve all the values present in a dictionary. It returns a special view object that displays a list of all the values in the dictionary.
When you call .values() on a dictionary, it doesn't give you a static list. Instead, it provides a dynamic view object. This view object reflects any changes made to the original dictionary. So, if you add, remove, or modify key-value pairs in the dictionary after calling values(), the view object will automatically update to reflect those changes.