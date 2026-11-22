# Q12. Find Common Elements
# Topic: List + Set
# Create two lists and find the common elements between them.
# Example:
# list1 = [10, 20, 30, 40, 50]list2 = [30, 40, 50, 60, 70]
# Expected output:
# Common elements: [30, 40, 50]
# Additional challenge: Find elements that exist in list1 but not in list2.
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
l1 = set(list1)
l2 = set(list2)
print(sorted(l1.intersection(l2)))
print(l1.difference(l2))
