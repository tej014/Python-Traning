# Write a recursive function to find the nth Fibonacci number.	Input: 6 → 8


def fib(num):
    if num == 0:
        return 0
    if num ==1:
        return 1
    return fib(num-1) + fib(num-2)

print(fib(6))
                              
    
    

