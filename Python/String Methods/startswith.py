text = "Python is a versatile language"

# Basic usage
print(text.startswith("Python"))  # Output: True
print(text.startswith("python"))  # Output: False (case-sensitive)
print(text.startswith("is")) #Output: False

# Using start parameter
print(text.startswith("is", 7))  # Output: True

# Using start and end parameters
print(text.startswith("versatile", 12, 20)) #Output: False
print(text.startswith("versatile", 12, 30)) #Output: True

# Using a tuple of prefixes
prefixes = ("Python", "Java", "C++")
print(text.startswith(prefixes))  # Output: True
