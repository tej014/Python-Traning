# Write a recursive function to print numbers from 1 to 10.

def print_num(num,start=1):
    if start==num+1:
        return 
    print(start)
    print_num(num,start+1)

print_num(23)