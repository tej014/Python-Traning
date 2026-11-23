# Q5. Find Even and Odd Numbers
# Topic: List + Conditions
# Take 10 numbers from the user and separate them into two lists: even numbers and odd numbers.
# Example:
# Input:  [1, 2, 3, 4, 5, 6]
# Even: [2, 4, 6]
# Odd:  [1, 3, 5]
n=[]
a = input("Enter number : ")
n.append(a)
b = input("Enter number : ")
n.append(b)
c = input("Enter number : ")
n.append(c)
d = input("Enter number : ")
n.append(d)
e = input("Enter number : ")
n.append(e)
f = input("Enter number : ")
n.append(f)
g = input("Enter number : ")
n.append(g)
h = input("Enter number : ")
n.append(h)
i = input("Enter number : ")
n.append(i)
j = input("Enter number : ")
n.append(j)
# n = ['45', '76', '12', '4', '72', '95', '15', '49', '59', '27']
print(n)
even = []
odd = []
if(int(n[0])%2 ==0):
    even.append(n[0])
else:
    odd.append(n[0])
if(int(n[1])%2 ==0):
    even.append(n[1])
else:
    odd.append(n[1])
if(int(n[2])%2 ==0):
    even.append(n[2])
else:
    odd.append(n[2])
if(int(n[3])%2 ==0):
    even.append(n[3])
else:
    odd.append(n[3])  
if(int(n[4])%2 ==0):
    even.append(n[4])
else:
    odd.append(n[4]) 
if(int(n[5])%2 ==0):
    even.append(n[5])
else:
    odd.append(n[5])
if(int(n[6])%2 ==0):
    even.append(n[6])
else:
    odd.append(n[6])
if(int(n[7])%2 ==0):
    even.append(n[7])
else:
    odd.append(n[7])
if(int(n[8])%2 ==0):
    even.append(n[8])
else:
    odd.append(n[8])
if(int(n[9])%2 ==0):
    even.append(n[9])
else:
    odd.append(n[9])
print(even)  
print(odd)