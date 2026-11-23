# Q3. Find the Largest Number
# Topic: List + Conditions
# Create a list of 5 numbers and find the largest number without using the max() function.
# Example:
# numbers = [12, 45, 23, 67, 10]
# Expected output:
# Largest number: 67
# Logic flow:
# 1. Create a list.
# 2. Assume the first element is the largest.
# 3. Compare it with every other element.
# 4. Update the largest value when necessary.
# 5. Print the result.
n = [12, 45, 23, 67, 10]
# print(max(n))
if(n[0]>n[1]>n[2]>n[3]>n[4]):
    print(n[0])
elif(n[1]>n[2]>n[3]>n[4]):
    print(n[1])
elif(n[2]>n[3]>n[4]):
    print(n[2])
elif(n[3]>n[4]):
    print(n[3])
else:
    print(n[4])