set1 = {1, 2, 3}
set2 = {1, 2}
set3 = {4, 5}

is_upperset1 = set1.issuperset(set2)
print(is_upperset1)  # Output: True (All elements of set2 are in set1)

is_upperset2 = set2.issuperset(set1)
print(is_upperset2)  # Output: False (3 is in set1 but not in set2)

is_upperset3 = set1.issuperset(set3)
print(is_upperset3)  # Output: False (No common elements)

is_upperset4 = set1.issuperset(set1)
print(is_upperset4)  # Output: True (A set is a superset of itself)

is_upperset5 = set1.issuperset(set())
print(is_upperset5) # Output: True (Any set contains the empty set)

# Another Example
required_skills = {"Python", "SQL"}
Applicants_skills_1 = {"Python", "SQL", "Java", "Data Analysis"}
Applicants_skills_2 = {"Python"}

is_upperset_A = Applicants_skills_1.issuperset(required_skills)
print(is_upperset_A)  # Output: True

is_upperset_B = Applicants_skills_2.issuperset(required_skills)
print(is_upperset_B)  # Output: False