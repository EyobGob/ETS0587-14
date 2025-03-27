text = "Python is a versatile language"

print(text.startswith("Python"))  # Output: True
print(text.startswith("python"))  # Output: False (case-sensitive)
print(text.startswith("is")) #Output: False

print(text.startswith("is", 7))  # Output: True

print(text.startswith("versatile", 12, 20)) #Output: False
print(text.startswith("versatile", 12, 30)) #Output: True

prefixes = ("Python", "Java", "C++")
print(text.startswith(prefixes))  # Output: True
