my_info = {"name": "Eyob", "age": 22, "city": "Addis Ababa"}

items_view = my_info.items()
print(items_view) # Output: dict_items([('name', 'Eyob'), ('age', 22), ('city', 'Addis Ababa')])

# Iterate through the key-value pairs in the items view
for key, value in items_view:
    print(f"Key: {key}, Value: {value}") 

''' Output:Key: name, Value: Eyob       
         Key: age, Value: 22
         Key: city, Value: Addis Ababa '''
