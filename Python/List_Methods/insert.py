my_list = [10, 20, 30]
my_list.insert(0, 5)
print(my_list)  # Output: [5, 10, 20, 30]

data = ['apple', 'banana', 'cherry']
data.insert(1, 'orange')
print(data)  # Output: ['apple', 'orange', 'banana', 'cherry']

numbers = [1, 2, 3]
numbers.insert(10, 4)  # Index is out of bounds, inserts at the end
print(numbers)  # Output: [1, 2, 3, 4]