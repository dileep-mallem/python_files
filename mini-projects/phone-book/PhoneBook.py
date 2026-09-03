# Build a contact book where each contact has a name (key) and details like phone number and email (stored as a tuple or list).
# Write a function add_contact(contacts, name, phone, email) that adds a new contact to the dictionary and returns the updated dictionary.
# Write a function search_contact(contacts, name) that returns the contact's details if found, or a "not found" message.
# Write a function delete_contact(contacts, name) that removes a contact.
# Print all contacts neatly (loop through the dictionary and display name, phone, email).
# Bonus: Keep a list of "recently searched" names to show search history.

data = {
    "Peddi" : (101 ,"peddi@gamil.com"),
    "Ojas Gambeera" : (1985 ,  "OG@SCUUniverse.ac.in"),
    "Sanjay Sahu" : (2008 , "Jalse@House.ac.in")
}

def add_contact(data,name,phno,email):
    data.setdefault(name,(phno , email))
    return data
 
flag=True
while(flag):
    print("1.Add 2.Search 3.delete 4.Display 5.Quit")
    n=int(input("Enter Choice : "))

    if n==1 :
        name=input("Enter Name : ")
        phno=int(input("Enter Phone Number : "))
        email=input("Enter Email : ")
        data=add_contact(data,name,phno,email)
        print("Data Added")
    elif n==2 :
        name=input("Enter NAme to serach : ").title()

        result=False
        for key , values in data.items():
            if key==name:
                result=True 
                break
        if result==True : 
            print("Person is FOund")
        else :
            print("Person Not Found")
    elif n==3:
        name=input("Enter NAme to Deete : ").title()

        result=False
        for key , values in data.items():
            if key==name:
                result=True 
                break
        if result==True : 
            del data[name] #deteltes
            # data.pop(name)  -> deletes and Return value
            print("Person is Deeted")
        else :
            print("Person Not Found")
    elif n==4 :
        for key , values in data.items():
            print(f"Name : {key} PhNo : {values[0]} Email : {values[1]}")
    elif n==5:
        flag=False  
    else :
        print("Enter Correct Choice")
    print("---------------") 
  

