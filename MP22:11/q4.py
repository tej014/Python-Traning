# Q14. Palindrome Checker
# Topic: String + Conditions
# Write a program to check whether a given word is a palindrome.
# A palindrome reads the same forward and backward.
# Examples:
# Input: madam
# Output: Palindrome
# Input: python
# Output: Not a Palindrome
# Additional challenge:
# - Make the program case-insensitive.
# - Ignore spaces in sentences.

p = input("Enter a string: ")
p = p.lower()
p = p.replace(" ", "")

l = list(p)

a = l.copy()
a.reverse()

if l == a:
    print("Palindrome")
else:
    print("Not a Palindrome")
