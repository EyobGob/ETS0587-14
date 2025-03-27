text = "filename.txt"

print(text.endswith(".txt"))  # Output: True
print(text.endswith(".TXT"))  # Output: False (case-sensitive)
print(text.endswith("file")) #Output: False

text2 = "This is a filename.txt"
print(text2.endswith(".txt", 10)) #Output: True

print(text.endswith(".txt", 0, 10)) #Output: False
print(text.endswith(".txt", 0, 12)) #Output: True