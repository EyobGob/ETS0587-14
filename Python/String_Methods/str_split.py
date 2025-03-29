text1 = "Hello World Python"
words1 = text1.split()
print(words1)  # Output: ['Hello', 'World', 'Python']

text2 = "Hello   World\tPython\nCode"
words2 = text2.split()
print(words2) # Output: ['Hello', 'World', 'Python', 'Code']

text3 = "apple,banana,orange"
fruits = text3.split(",")
print(fruits)  # Output: ['apple', 'banana', 'orange']

text4 = "1:2:3:4:5"
numbers = text4.split(":")
print(numbers) #output: ['1', '2', '3', '4', '5']