# Write a recursive function to calculate the sum of numbers from 1 to N.
def fact(num):
    if num == 0:
        return 1
    return fact(num-1) * num

x = fact(5)
print(x)

