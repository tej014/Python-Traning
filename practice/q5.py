# Q4. Remove Duplicates
# Topic: List + Set
# Write a program to remove duplicate elements from a list.
# Example:
# numbers = [1, 2, 3, 2, 4, 1, 5]
# Expected output:
# [1, 2, 3, 4, 5]
n = [1, 2, 3, 2, 4, 1, 5]
print(list(set(n)))

# a = set()
# a.update(n)
# n = []
# n.append(a)
# print(n)