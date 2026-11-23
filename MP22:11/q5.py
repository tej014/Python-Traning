products = {    "Laptop": 50000,    
                "Mouse": 500,      
                "Keyboard": 1000,    
                "Monitor": 10000
            }
print(list(products.items()))
ind = 0
i = 1
while ind<=3:
    print(list(products.keys())[ind],"-->",i)
    ind = ind + 1
    i = i+1

x = int(input("Select a product from a list : "))
ind = x - 1
p = list(products.values())[ind]
x = list(products.keys())[ind]
print("You have selected",x)
print(x,"is for",p,"₹")

q = int(input("Select quantity for "))
print("Added",q,x,"to your cart")

z = str(input("For proseed further type (yes/no)"))

if z=="yes":
    t = q*p
    print("your total bill is",t)
    if (t)>=50000:
        d = t/10
        f=t-d
        print("discount addes 10 %")
        print("You have to pay",f,"₹")
else:
    print("Thank you for visiting our shop :)")


####### polish version of this code is on q5i.py file please check ##########
#### this is the mini project of Shopping Cart System