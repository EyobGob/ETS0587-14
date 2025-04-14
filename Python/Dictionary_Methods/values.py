# Basic usage
student = {"name": "Eyob", "age": 22, "major": "Electro_Mechanical"}
all_values = student.values()
print(all_values) # Output: dict_values(['Eyob', 22, 'Electro_Mechanical'])

# Iterating through the values
grades = {"Applied": 95, "Mechanics": 88, "Design": 92}
print("Student's grades:")
for grade in grades.values():
    print(grade)
''' Output: Student's grades:
95
88
92'''

# Checking if a value exists
inventory = {"apples": 10, "bananas": 25, "oranges": 15}
if 25 in inventory.values():
    print("Bananas are in stock.") 
else:
    print("Bananas are out of stock.")
# Output: Bananas are in stock.