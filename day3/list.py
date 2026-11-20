#lists are the built in data type that store set of value
#it can store elements of diffrent datatypes like int,bool,string,floating.
# list are mutable

marks = [75,35,84,56,35,75,36,90,68,83,46]
# print(len(marks))
# print(type(marks))
# print(marks[::-1])
# print(marks[3])

# students = ["karan",50,"kamal",56.43,37,26,True]
# print(students)
# students[2]="rajesh" #"<=====mutble"
# print(len(students))
# students[6]=False #"<=====mutble"
# print(students)
# students[6]=True
# print(students.index(True))
# print(students)

#list methode

list = [2,1,4,3]
print("1",list)
list.append(5)
print("2",list)
list.sort()
print("3",list)
list.sort(reverse=True)
print("4",list)
list.reverse()
print("5",list)
list.insert(3,9)
print("6",list)
list.remove(2)
print("7",list)
list.pop(3)
print("8",list)
list.pop(2)
print("9",list)