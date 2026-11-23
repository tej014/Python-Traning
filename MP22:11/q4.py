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

x = "Madam"
x = x.lower()
x = x.replace(" ","")
a = list(x)
y = a.copy()
y.reverse()
print(y)
if y==a:
    print("Palindrome")
else:
    print("not Palindrome")


