set_p = {1, 2, 3, 4, 5}
set_q = {3, 5, 6, 7}

# Find elements that are in set_p or set_q, but not both
symmetric_difference_pq = set_p.symmetric_difference(set_q)
print(f"Symmetric difference of set_p and set_q: {symmetric_difference_pq}")  
# Output: Symmetric difference of set_p and set_q: {1, 2, 4, 6, 7}

set_r = {1, 2, 3}
# Symmetric difference with a subset
symmetric_difference_pr = set_p.symmetric_difference(set_r)
print(f"Symmetric difference of set_p and set_r: {symmetric_difference_pr}")  
# Output: Symmetric difference of set_p and set_r: {4, 5}

set_s = {1, 2, 3, 4, 5}
# Symmetric difference with an identical set results in an empty set
symmetric_difference_ps = set_p.symmetric_difference(set_s)
print(f"Symmetric difference of set_p and set_s: {symmetric_difference_ps}")  
# Output: Symmetric difference of set_p and set_s: set()