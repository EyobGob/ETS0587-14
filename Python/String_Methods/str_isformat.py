format1 = "{} {}".format("hello", "world")  # Output: 'hello world'
print(format1)

format2 = "{1} {0}".format("hello", "world")  # Output: 'world hello'
print(format2)

format3 = "{name} is {age} years old".format(name="Alice", age=30)  # Output: 'Alice is 30 years old'
print(format3)