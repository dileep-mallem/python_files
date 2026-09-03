#Hollow Sqaure 
 #Taking Number as Inout
n=int(input("Enter Number : "))
for i in range(1,n+1):
    if i==1 or i==n :
        for j in range(1,n+1):
            print("*",end=" ")
        print()
    else :
        for j in range(1,n+1):
            if j==1 or j==n:
                print("*",end=" ")
            else :
                print(" ",end=" ")
        print()
print()


#Diamond
 #First Up  (First Left spaces and star) then right Triabl

for i in range(1,n+1,2):
    for j in range(1,n-i,2):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(n-i,1,-2): #mid-1 == 2 heare 2,1,0
        print(" ",end=" ")
    print() #NEaxt Row
#Bottom Pyramid
for i in range(1,n,2):
    for j in range(1,i+1,2):
        print(" ",end=" ")
    for j in range(1,n-i,1):
        print("*",end=" ")
    for j in range(1,i+1,2):
        print(" ",end=" ")
    print()
print()


    

    


    


        
