# Q13. Student Marks Management
# Topic: Dictionary + Conditions + List
# Create a dictionary containing 5 students and their marks.
# Example:
# students = {    "Tej": 85,    "Rahul": 45,    "Amit": 92,    "Sneha": 35,    "Priya": 76}
# Your program should:
# 1. Display all students and their marks.
# 2. Find the student with the highest marks.
# 3. Find the student with the lowest marks.
# 4. Calculate the average marks.
# 5. Display students who passed (marks >= 40).
# 6. Display students who failed.
students = {    "Tej": 85,
                "Rahul": 45,
                "Amit": 92,
                "Sneha": 35,
                "Priya": 76
            }
print(list(students.items()))
# high = max(students.values())
print(max(students, key=students.get))
print(min(students,key=students.get))
total = sum(students.values())

avg = total / len(students)
print(avg)
x = list(students.values())
