list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

letters = ['p', 'q']
word = "rs"
letters.extend(word)
print(letters)  # Output: ['p', 'q', 'r', 's']