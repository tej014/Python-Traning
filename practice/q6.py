# Q6. Tuple Operations
# Topic: Tuple
# Create a tuple containing 5 numbers.
# Perform these operations:
# 1. Print the first element.
# 2. Print the last element.
# 3. Find the length of the tuple.
# 4. Check whether number 10 exists.
# 5. Count how many times number 5 appears.

x = (1,2,3,4,5,6,7,8,9,10,2,7,4,1,9,1,6,4,8,2,4,10)
print(x[0])
print(len(x))
if(int(x.count(10))):
    print("Yes 10 is available")
else:
    print("Yes 10 is not available")

print(x.count(5))
y = (list(set(x)))
print(y)