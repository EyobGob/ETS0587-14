fruit_colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

fruit_keys = fruit_colors.keys()
print(fruit_keys) # Output: dict_keys(['apple', 'banana', 'grape'])

print("\nThe fruits are:") 
for key in fruit_keys:
    print(key)

'''Output:
The fruits are:
apple
banana
grape'''

if "banana" in fruit_keys:
    print("\nYes, 'banana' is a fruit in our dictionary.") # Output: Yes, 'banana' is a fruit in our dictionary.

print("-------------------------------------------------------------------------------")

student_grades = {"Abebe": 85, "Alemu": 92, "Mikiyas": 78}
student_keys = student_grades.keys()
print(student_keys) # Output: dict_keys(['Abebe', 'Alemu', 'Mikiyas'])

# Add a new student
student_grades["Gashaw"] = 95
print(student_keys)  # Output: dict_keys(['Abebe', 'Alemu', 'Mikiyas', 'Gashaw'])

# Remove a student
del student_grades["Alemu"]
print(student_keys) # Output: dict_keys(['Abebe', 'Mikiyas', 'Gashaw'])
