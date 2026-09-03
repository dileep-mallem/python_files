n=int(input("Enter Number : "))

#Printing Prime Numbers from 2 to n

print(f"Prime Numbers upton {n} are ")
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0 :
            count +=1
        
    if count == 2 :
        print(i,end=" ")
print()
