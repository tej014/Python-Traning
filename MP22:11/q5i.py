# Q15. Shopping Cart System
# Topic: List + Dictionary + Conditions + Tuples
# Create a basic shopping cart program.
# Products:
# products = {    "Laptop": 50000,    "Mouse": 500,    "Keyboard": 1000,    "Monitor": 10000}
# Requirements:
# 1. Display all available products and prices.
# 2. Ask the user which product they want.
# 3. Ask for the quantity.
# 4. Add the product and quantity to the cart.
# 5. Calculate the total bill.
# 6. Apply a 10% discount if the bill exceeds ₹50,000.
# 7. Display the final bill.
# Logic flow:
# Start shopping
# Display available products
# Select product and quantity
# Calculate total bill
# Bill exceeds ₹50,000?
# Yes
# Apply 10% discount
# No
# No discount
# Display final bill

products = {    "Laptop": 50000,    
                "Mouse": 500,      
                "Keyboard": 1000,    
                "Monitor": 10000
            }
print(list(products.items()))

a = int(input("count of products :-> "))
ind = 0
b=1
c=1
total=0
while b<=a:
    print("Select",b,"product : ")
    while ind<=3 and c<=4:
        print(list(products.keys())[ind],"--->",c)
        ind+=1
        c+=1
    b+=1
    d = int(input("select a product from a list :-> "))
    ind = d-1
    e = list(products.values())[ind]
    f = list(products.keys())[ind]
    print("the price for",f,"is",e,"₹")
    g = int(input("Quentity of product :-> "))
    print("you want",g,f)
    total = total + e * g 
    print("total bill",total) 

   
h = str(input("You want to procees further (yes/no) : "))

if h=="yes":
    if total>=50000:
        discount = total/10
        pay = total-discount
        print("you have got discount 10","%","discount pay -->",pay,"₹")
    else:
        print("No discount pay -->",total,"₹")
else:
    print("Thank you for visiting our shop :")


 #### this is the mini project of Shopping Cart System
 # Thank you for visiting