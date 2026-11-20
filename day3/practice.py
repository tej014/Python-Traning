list = []
a = input()
list.append(a)
b = input()
list.append(b)
c = input()
list.append(c)
print(list)
###############################
list = ['r','a','c','e','c','a','r']
a = list.copy()
print(a)
a.reverse() 
b = a
print(b)

if(list == b):
    print("It is palindrom")
else:
    print("not palindrom")

###################################

grades = ['C','D','A','A','B','B','A']
x = grades.count("A")
print(x,"Students socred A Grade")
grades.sort()
print(grades)

####################################

