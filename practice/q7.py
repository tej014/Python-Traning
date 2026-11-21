# Q7. Student Information
# Topic: Dictionary
# Create a dictionary containing student information.
# student = {    "name": "Tej",    "age": 23,    "course": "Python",    "marks": 85}
# Perform these operations:
# 1. Print the student's name.
# 2. Print the student's age.
# 3. Update marks to 90.
# 4. Add a new key called city.
# 5. Print all dictionary keys and values.

student = { 
    "name": "Tej", 
    "age": 23,   
    "course": "Python",  
    "marks": 85
    }
print(student)
print("name od student is : ",student["name"])
print("age of student is :",student["age"])
student.update({"marks":90})
print("update marks :",student["marks"])
student.update({"city":"Pune"})
print("new city addes",student["city"])
print(student.items())