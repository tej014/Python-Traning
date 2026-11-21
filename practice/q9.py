# Q9. Positive, Negative or Zero
# Topic: Conditional Statements
# Take a number from the user and check whether it is:
# - Positive
# - Negative
# - Zero
# Example:
# Input: -10
# Output: Negative Number

num = int(input("enter a number "))
print(num)
if(int(num)>0):
    print(num,"number is positive ")
elif(int(num)<0):
    print(num,"number is negative ")
else:
    print(num,"number is zero")
    