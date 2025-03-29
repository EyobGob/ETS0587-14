text1 = "   Hello, World!   "
stripped_text1 = text1.rstrip()
print(stripped_text1)  # Output: "   Hello, World!"

text2 = "example.comwww"
stripped_text2 = text2.rstrip("w")
print(stripped_text2)  # Output: "example.com"

text3 = "123abc456cba"
stripped_text3 = text3.rstrip("abc")
print(stripped_text3) #output: "123abc456"

text4 = "stringcccbbbbaa"
stripped_text4 = text4.rstrip("abc")
print(stripped_text4) #output: "string"