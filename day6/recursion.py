###recursion

#function calls itself repeatidely
# to solve smaller versions of a problem, and every recursive function
# must include a base case and a recursive case to avoid infinite loops. 
# Common examples include factorial, Fibonacci, and list processing, 
#  and Python enforces a recursion depth limit of about 1000 calls by default.

# def show(n):
#     if n==0: #<----- base casse it also called as condition
#         return
#     print(n)
#     show(n-1)
#     print("end")
    

# show(5)
# show(5)
# show(4)
# show(3)
# show(2)
# show(1)
# # show(5)
# for x in range(5,0,-1):
#     show(x)

#factorial

# def fact(n):
#     if n==1:
#         return 1
#     return fact(n-1)*n

# print(fact(5))