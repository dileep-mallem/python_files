#INput And Output
name1=input("Enter Yuour Name : ")
print(f"Hello, {name1}! Welcome to Python.")

age1=int(input("EnterD Your Age : "))
print(f"You are {age1+10} Old in 10 Years ")
print("You are "+str(age1+10)+" Old in 10 Years ") #Can Concatenate Only Strings 

length=float(input("Enter Length : "))
width=float(input("Enter Width : "))
print(f"Are of Rectangle : {length*width}")

item_name=input("Enter Item Name: ")
qty=int(input("Enter Quantity : "))
price_per_unit=float(input("Enter Price per Unit : "))

print(f"Item : {item_name} | Qty : {qty} | Total : {qty*price_per_unit}")