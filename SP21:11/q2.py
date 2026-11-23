# Write a program to count the total number of vowels in a given string.
# ExaExample:
# Input:  programming
# Output: 3


# Logic flow:
# 1. Take a string.
# 2. Create a variable count = 0.
# 3. Check each character.
# 4. If it is a vowel (a, e, i, o, u), increase count.
# 5. Print the count.

# s = ['p','r','o','g','r','a','m','m','i','n','g']
# s = "programming"
s = input("Enter a String : ")
count = s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")
print(count)