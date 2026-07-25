#Username is no more than 12 cuhars 
#user name must not contain spaces and digts

username=input("Enter a username: ")

if len(username)<=12 : 
    if username.find(" ")==-1 : #can use .count(" ") also 
        if username.isalpha()==True :
            print("Username is Valid")
        else : 
            print("User name Should not conatain Any Digits")
    else : 
        print("User name Should not conatain Any Spaces")
else : 
    print("User name Should not conatain more than 12 characters")


#elif not username.find(" ")==-1 , if not true then pass next  Conditional Statremnt , if true like ==-1 then statement executes 