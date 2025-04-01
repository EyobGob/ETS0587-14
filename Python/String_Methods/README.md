# STRING METHODS

# Day1
# str.lower() Method
The str.lower() method in Python is a built-in string method that converts all uppercase characters in a string to lowercase. It does not modify the original string but instead returns a new string with the modifications. This method is particularly useful for standardizing text (e.g., for case-insensitive comparisons or processing user input).

# str.upper() Method
The str.upper() method in Python is a built-in string method that converts all lowercase alphabetic characters in a string to uppercase. Like str.lower(), it creates a new string and leaves the original string unchanged. This method is handy for standardizing text to uppercase, especially for formatting or case-insensitive processing.

# str.capitalize() Method
The str.capitalize() method in Python is a built-in string method that capitalizes the first character of a string while converting all other characters to lowercase. This is especially useful for formatting strings into a sentence-like structure.

# Day2
# str.title() Method
In Python, the str.title() method is used to capitalize the first letter of each word in a string while converting all other letters in the word to lowercase. It's a handy method for formatting text into a title-like style.

# str.swapcase() Method
The str.swapcase() method in Python is used to reverse the case of each character in a string. It converts lowercase letters to uppercase and uppercase letters to lowercase. This can be useful when working with case conversions or for stylistic purposes.

# str.find() Method
The str.find() method in Python is used to locate the position of a specified substring within a string. It returns the index of the first occurrence of the substring if found, or -1 if the substring isn't found.

# Day3
# str.index() Method
The str.index() method is used to find the index (position) of the first occurrence of a substring within a given string. It's a fundamental string manipulation tool in Python.

# str.startswith() Method
The str.startswith() method in Python is a powerful tool for checking if a string begins with a specific prefix. Here's a comprehensive overview:
The primary function of str.startswith() is to determine whether a given string begins with a specified substring (prefix).
It returns a Boolean value: True if the string starts with the prefix, and False otherwise.

# str.endswith() Method
The str.endswith() method in Python mirrors str.startswith() but checks the end of a string instead of the beginning. Here's a comprehensive look:
str.endswith() determines if a string ends with a specified suffix (substring).
It returns a Boolean value: True if the string ends with the suffix, and False otherwise.

# Day4
# str.count() Method
The str.count() method in Python is a built-in string function that returns the number of non-overlapping occurrences of a substring within a given string. Here's a comprehensive discussion:

# str.replace() Method
The str.replace() method in Python is used to create a new string where all occurrences of a specified substring (old) are replaced with another substring (new).

# str.strip() Method
The str.strip() method in Python is a powerful tool for cleaning up strings by removing unwanted leading and trailing characters. Here's a breakdown of its functionality:
By default, strip() removes leading and trailing whitespace characters. This includes spaces, tabs (\t), and newline characters (\n).
You can provide an optional chars argument to strip(). This argument is a string specifying the set of characters you want to remove from the beginning and end of the original string.

# Day5
# str.lstrip() Method
str.lstrip() is a built-in string method in Python that returns a copy of the string with leading characters removed.
The primary purpose of str.lstrip() is to remove whitespace characters (spaces, tabs, newlines) from the left side (beginning) of a string.
It can also remove any specified set of characters from the left side.

# str.rstrip() Method
str.rstrip() is designed to remove trailing characters (characters at the end or right side) from a string.
Similar to lstrip(), it primarily handles the removal of trailing whitespace (spaces, tabs, newlines) but can also remove any specified set of characters.

# str.split() Method
str.split() is a fundamental string method in Python used to break a string into a list of substrings.
The primary purpose of str.split() is to divide a string into smaller parts based on a specified delimiter.
It's commonly used for parsing strings, processing text data, and extracting information from strings.

# Day6 
# str.join() Method
The str.join(iterable) method is a powerful tool for concatenating strings within an iterable (like a list, tuple, or set) using a specified string as a separator.
This is the string that will be inserted between each element of the iterable.
It can be any string, including an empty string ("").

# str.isalpha()
The str.isalpha() method is a string method that checks if all characters in a string are alphabetic (letters).
It returns True if all characters in the string are letters (a-z, A-Z).
It returns False if the string contains any non-alphabetic characters (numbers, symbols, spaces, etc.).
It returns False if the string is empty.

# str.isdigit()
The str.isdigit() method is a string method that checks if all characters in a string are digits (0-9).
It returns True if all characters in the string are digits.
It returns False if the string contains any non-digit characters (letters, symbols, spaces, etc.).
It returns False if the string is empty.

# Day7
# str.isalnum() Method
The str.isalnum() method is a handy tool for checking if a string consists entirely of alphanumeric characters.
The isalnum() method examines a string and returns True if all characters within that string are alphanumeric.

"Alphanumeric" means that the characters are either letters (a-z, A-Z) or numbers (0-9).
If the string contains any characters that are not letters or numbers (such as spaces, punctuation marks, or special symbols), isalnum() returns False.
An empty string returns False.

# str.isspace() Method
The str.isspace() method in Python is designed to check if a string consists entirely of whitespace characters. Let
str.isspace() evaluates a string and returns True if all characters within the string are whitespace.
If the string contains any non-whitespace characters, str.isspace() returns False.
An empty string returns False.

# str.format() Method
The str.format() method in Python is a powerful and versatile way to format strings. It allows you to insert values into placeholders within a string, making it easy to create dynamic and readable output. 
str.format() replaces placeholders (curly braces {}) within a string with specified values.
Placeholders can be either:
Implicitly numbered (based on the order of arguments).
Explicitly numbered (using indices).

# Day8
# f-strings
F-strings, or formatted string literals, are a powerful and convenient way to embed expressions inside string literals for formatting. They were introduced in Python 3.6 and offer a more readable and concise syntax compared to older string formatting methods like % formatting or .format().

# len() function
The len() function in Python is a built-in function used to determine the length of an object. It's a versatile tool that can be applied to various data types, primarily sequences and collections.
The primary purpose of len() is to return the number of items in an object.
"Items" can refer to characters in a string, elements in a list or tuple, key-value pairs in a dictionary, or items in a set.

# str.encode() Method
In Python, the str.encode() method is fundamental for converting a string into a sequence of bytes. This is crucial because computers ultimately work with bytes, and when you need to store or transmit text data, it must be encoded into a byte format. 
The str.encode() method translates a Unicode string into a byte sequence. 
This is essential for saving text to files, sending text over networks & interacting with systems that require byte data.
