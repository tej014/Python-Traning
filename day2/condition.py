
#conditions statements

"""
if (statement)
elif(statement)
elif(statement)
else(statement) 
"""

# age = 14
# if(age>=18):
#     print("you can vote")
# elif(age<=18):
#     print("you cannot vote")
# else:
#     print("you are under 18")


#grade sutdents based on marks

# marks = int(input("Enter your marks : "))

# if(marks>=90):
#     print("A Grade")
# elif(marks>=80 and marks<90):
#     print("B Grade")
# elif(marks>=70 and marks<80):
#     print("C Grade")
# elif(marks>=60 and marks<70):
#     print("D Grade")
# else:
#     print("You are failed!!")



#nesting ----> writing another statement inside statement

age = int(input("Enter your age :"))
if(age>=18):
    if(age>=85):
        print("You cannot Drive")
    else:
        print("you can drive")
else:
    print("You Cannot drive")