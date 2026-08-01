# Simulate a small store where items have prices and quantities, and a customer "buys" a few items, generating a bill.
# Create an inventory dictionary where values are tuples of (price, quantity_available):
# Create a shopping cart as a list of tuples: cart = [("Rice", 2), ("Oil", 1)]
# Write a function calculate_total(item_name, quantity, inventory) that returns the cost for that item (price * quantity).
# Loop through the cart, calculate the total bill amount, and print an itemized bill.
# Write a function update_inventory(inventory, item_name, quantity_sold) that reduces the available quantity after purchase and returns the updated inventory.
# Print the final inventory after the purchase.
# Bonus: Add a check — if requested quantity is more than available stock, print "Insufficient stock" instead of processing that item.

inventory = {
    "Rice" : (1500 , 5),
    "Maggi" : (160 , 56) ,
    "Peanut Butter " : (300 , 15),
    "Almonds" : (450 , 6)  
    }

cart=[]
for item , values in inventory.items():
    cart.append((item , values[1]))
print(cart)

def calculate_total(data,item_name,quantity):
    price=0
    for item,details in data.items():
        if item==item_name:
            price=details[0]
    cost = price *quantity
    return cost 

for item , details in inventory.items():
    total_amount=details[0] * details[1] 
    print(f"Item : {item} Total Amount : {total_amount}")
print("------------")

def update_inventory(data,item_name,quanity_sold):
    for item,details in data.items():
        if item==item_name:
            list1=list(details) #Tuple converting to List(Mutable)
            list1[1]=list1[1]-quanity_sold 
            details=tuple(list1) #vonverts into Tuple from List
            data[item]=details  #Updtaes 
    return data 

#Total cost of Purchased Item 
x="Maggi"#Input("Enter The Item You want to Purchase : ").title()
y=20
cost=calculate_total(inventory,x,y)
print(f"Item : {x} Total Cost : {cost}")
#Update 
print(update_inventory(inventory,x,y))






