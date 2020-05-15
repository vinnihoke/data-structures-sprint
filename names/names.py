import time
# import sys
# sys.setrecursionlimit(11000)
from sll import SLL
from bst import BST


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# * Return the list of duplicates in this data structure
# Replace the nested for loops below with your improvements
# Grabbing a name from names_1 list
# for name_1 in names_1:
#     # Checking for a match in names_2
#     for name_2 in names_2:
#         # If there is a match add to duplicates.
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ? Using set and intersect.
# duplicates = list(set(names_1).intersection(set(names_2)))
# https://www.w3schools.com/python/ref_set_intersection.asp
# Creates a list with a set from names_1. Intersection is the difference between the two lists, therefore all the duplicates. We pass in another set from names_2.
# Complexity is (n-1)*O(l) where l is max(len(s1),..,len(sn))
# https://wiki.python.org/moin/TimeComplexity
# runtime: 0.004992008209228516 seconds

# ? Using list comprehension.
# duplicates = [name for name in names_1 if name in names_2]
# This implementation should be O(n^2). It still needs to loop over each element and run a looped if check in names because of the "in" keyword.
# runtime: 1.5957581996917725 seconds

# ? Using SLL.
# sll = SLL()

# for name in names_1:
#     sll.add_to_tail(name)

# for name in names_2:
#     if sll.search(name):
#         duplicates.append(name)
# Worked but DAMN lol!!! O(c^n)
# runtime: 32.25076985359192 seconds

# ? Using BST
# runtime: 0.17090082168579102 seconds
# O(log n)
bst = BST("")

for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
