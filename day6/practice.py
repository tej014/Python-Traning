# def lenlist(list):
#     print(len(list))

# x = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15]

# lenlist(x)
# print(x[3],end=" ")
# print(x[4],end="\n")
# print(x[5],end=" ")
# print(x[6])

# def printlist(a):
#     for item in a:
#         print(item,end=" ")

# printlist(x)
# print()

#wrp to find factorial

# def factorial(x):
#     num = x
#     i = 1
#     fact = 1
#     while i<=num:
#         fact=fact*i
#         i=i+1
#     x = fact
#     print(x)
#     return x

# factorial(7)

# def factoria(x):
#     fact = 1
#     for y in range(1,x+1,1):
#         fact = fact * y
#     print(fact)    
#     return fact
# factoria(5)    

# WAP tp convert usd to inr

def currencyconverter(usd):
    inr = 92.72 * usd
    print(inr) 
    return inr

currencyconverter(5)