text1 = "   Hello, World!   "
stripped_text1 = text1.lstrip()
print(stripped_text1)  # Output: "Hello, World!""

text2 = "www.example.com"
stripped_text2 = text2.lstrip("w.")
print(stripped_text2)  # Output: "example.com"

text3 = "abababacstring"
stripped_text3 = text3.lstrip("ab")
print(stripped_text3) # Output: "cstring"