# Q10. Password Length Checker
# Topic: String + Conditions
# Write a program that accepts a password and checks its length.
# Conditions:
# - Less than 6 characters → Weak password.
# - 6–10 characters → Medium password.
# - More than 10 characters → Strong password.

x = str(input("Enter a Password : "))
print(x)
print(len(x))
if(len(x)<6):
    print("Weak password.")
elif(6<=len(x) and 10>=len(x)):
    print("Medium password.")
else:
    print("Strong password.")
