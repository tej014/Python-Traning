# def lenlist(list):
#     print(len(list))

# x = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15]c

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

# def currencyconverter(usd):
#     inr = 92.72 * usd
#     print(inr) 
#     return inr

# currencyconverter(5)

##recursion practice questions


# def fact(n):
#     n
#     i=1
#     count = 1
#     while i<=n-1:
#         count = count * (i+1)
#         i=i+1
#         x = count
#     print(x) 
#     return x      
# fact(5)

# def countfact(n):
#     fact=1
#     for i in range(1,n):
#         fact = fact * (i+1)
#     print(fact) 
# countfact(5)

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return fact(n-1)*n

# print(fact(5))

#WAP to calculate sum of firt n natural numbers using recursion


# def calsum(n):
#     if n == 0:
#         return 0
#     return calsum(n-1)+n

# print(calsum(4))


#WAP to print all elements from list using recurtion and function use list and index hint


# def printlist(lst,ind=0):
#     lst[ind]=len(lst)
#     print(lst,lst[ind])
#     return
# list = [1,2,3,4,5]
# printlist(list)

def printlist(lst,ind=0):
    if(ind==len(lst)):
        return
    print(lst[ind])
    return printlist(lst,ind+1)

x = ["a","b","f","c","d","e"]
printlist(x)

# printlist(x,0)
# printlist(x,3)
# printlist(x,4)
# printlist(x,5)

# i=0
# l=len(x)
# while i<l:
#     printlist(x,i)
#     i = i+1