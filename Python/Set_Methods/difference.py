set_x = {10, 20, 30, 40, 50}
set_y = {30, 50, 60}
set_z = {40, 80}

# Find elements in set_x but not in set_y
difference_xy = set_x.difference(set_y)
print(difference_xy)  # Output: {40, 10, 20}

# Find elements in set_x but not in set_y and not in set_z
difference_xyz = set_x.difference(set_y, set_z)
print(difference_xyz)  # Output: {10, 20}

set_w = {10, 20}
# Difference with a subset
difference_xw = set_x.difference(set_w)
print(f"Elements in set_x but not in set_w: {difference_xw}")  # Output: Elements in set_x but not in set_w: {40, 50, 30}

# Difference with a superset results in an empty set
difference_wx = set_w.difference(set_x)
print(f"Elements in set_w but not in set_x: {difference_wx}")  # Output: Elements in set_w but not in set_x: set()

# By using the "-" operator
difference_xy_operator = set_x - set_y
print(difference_xy_operator)  # Output: {40, 10, 20}

difference_xyz_operator = set_x - set_y - set_z
print(difference_xyz_operator)  # Output: {10, 20}