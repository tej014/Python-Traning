# functions in pythone

# there are two type of functions in pythn 

# 1) built-in function
# print() range() len() type()


# 2) user define function
# the founction programmer write it is user define


#Default parematers
# assigng a default value to parameter, which is used when no argument is passed
# assing defaulf always from last

# def cal_prod(a,b):
#     print(a*b)
#     return a*b
# cal_prod() #-------> this will throw error

# def cal_prod(a=1,b=1):
#     print(a*b)
#     return a*b
# cal_prod() #--->>start assign from last

# def cal_prod(a,b=2):
#     print(a*b)
#     return a*b
# cal_prod(3) ----> if we assign a and b in call it will throw error