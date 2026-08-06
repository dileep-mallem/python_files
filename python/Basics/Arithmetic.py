#Arithmetic and math
import math

a=int(input("Enter First Number : "))
b=int(input("Enter First Number : "))

print(f"Sum : {a+b} Diff : {a-b} Product : {a*b} Quotient : {a/b}") #a/b=0.625 for 5 and 8 .It automatically Converts

if(a%2==0):
    print(str(a)+" is Even")
else:
    print(str(a)+" is Odd")

#Terinary 
label="Even" if  b%2==0 else "Odd"
print(label)

rad=float(input("Enter Circle Radius : "))
print("Area of Circle : "+str(math.pi*rad*rad))

temp_inC=float(input("Enter Temp in Celsius : "))
f=(temp_inC*(9/5))+32
print("Temp in Farh is "+str(f))
