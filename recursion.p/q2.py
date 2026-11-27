# Write a recursive function to print numbers from 10 to 1.

def print_num(num):
    if num == 0:
        return 0
    print(num)
    print_num(num-1)

print_num(7)