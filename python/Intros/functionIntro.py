# Function = A block of reusable code 
#               place () after a function name to invoke it 

# return = statement used to end a function 
#           and send a result back to the caller

def happy_birthday(name,age): #name = parameter(Temporary Variable)
    print(f"Happy birthday to u {name} !!")
    print(f"You are {age} yerasOld")
 
happy_birthday("Dileep",20) #Arguments 
happy_birthday("Jon Sow",34)

print()
print()

def display_invoice(username , amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date} ")

display_invoice("Dileep",50.87,"01/01")

print()

def add(x,y):
    return x+y 
def subract(x,y):
    return x-y 
def multiply(x,y):
    return x*y 
def divide(x,y):
    return x/y 
print(add(1,2))
print(subract(1,45))
print(divide(3,4))


print() 

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last 
full_name=create_name("dileep","kumar")
print(full_name)