text = "filename.txt"

# Basic usage
print(text.endswith(".txt"))  # Output: True
print(text.endswith(".TXT"))  # Output: False (case-sensitive)
print(text.endswith("file")) #Output: False

# Using start parameter
text2 = "This is a filename.txt"
print(text2.endswith(".txt", 10)) #Output: True

# Using start and end parameters
print(text.endswith(".txt", 0, 10)) #Output: False
print(text.endswith(".txt", 0, 12)) #Output: True