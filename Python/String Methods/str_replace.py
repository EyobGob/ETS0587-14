text = "Hello, World! Hello, Python!"

new_text = text.replace("Hello", "Hi")
print(new_text)  # Output: Hi, World! Hi, Python!

new_text_one_replace = text.replace("Hello", "Hi", 1)
print(new_text_one_replace) #Output: Hi, World! Hello, Python!
