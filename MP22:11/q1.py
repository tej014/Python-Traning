# Q11. Character Frequency Counter
# Topic: String + Dictionary
# Write a program to count how many times each character appears in a string.
# Example:
# Input: banana
# Output:
# b: 1
# a: 3
# n: 2
# Logic flow:
# 1. Take a string.
# 2. Create an empty dictionary.
# 3. Iterate through each character.
# 4. Check whether the character already exists.
# 5. If yes, increase its count.
# 6. Otherwise, initialize its count to 1.
# 7. Display the dictionary.

s = "banana"
print(list(s))
print("b:",s.count("b"))
print("a:",s.count("a"))
print("n:",s.count("n"))