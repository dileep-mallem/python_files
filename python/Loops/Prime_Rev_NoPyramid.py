#Taking Wholw Number as Input
n=int(input("Enter Whole Number : "))

#Prime Checking : Number Div by 1 and Itself Only
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
    else :
        continue 
print()
label="Prime" if c==2  else  "Not PRime"
print(f"{n} is {label}")
print()

#Reverse a Num sing While Loop by Below or Convert to String and Revrese it using Revrse Loop
original = int(input("Enter Number : "))
num=original
rev=0
while num!=0:
    rem=num%10
    rev=rev*num+rem 
    num/=10
print()
print(f"Revese of {original} is {rev}")

print()

#Number Pyramig




