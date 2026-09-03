# cal fun  , two and operator  as Input , solve them , ask user to continue with reslut or new calcuation or Quit
import math

def calculator():
    n1=int(input("Enter first Number : "))

    flag=True
    while(flag):
        result=None
        op=input("Enter Operation(+ , - , * , / , % , ^ ) : ")
        n2=int(input("Enter Second Number : "))
            
        if op=='+':
            result=n1 + n2 
        if op=='-':
                result=n1 - n2 
        if op=='*':
                result=n1 * n2 
        if op=='/':
                result=n1 / n2 
        if op=='%':
                result=n1 % n2 
        if op=='^':
                result=math.pow(n1,n2)
        print(f"Result : {result}")
        print("----------")
    
        continue_flag=input("Enter 'y' if u to continue or 'n' to start new calculation or any other to Quit : " ).lower()

        if continue_flag=='y':
                n1=result # result points to n1 
        elif continue_flag=='n' :
                calculator()
        else :
                flag=False            
print("--------------")
calculator()

     

