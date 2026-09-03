email=input("Enter Your Email : ")

if email.find("@")==-1 : 
    print("Email Should Contain @")
else : 
    if email.endswith(".com")==True or email.endswith(".in"):
        print("Valid Email")
    else : 
        print("Email Shouls endswtih .com or .in")
print()