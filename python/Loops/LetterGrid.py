rows=int(input("Enter No of Rows : "))
cols=int(input("Enter No of Columns : "))

for i in range(1,rows+1):
    for j in range(1,cols+1):
        print(f"{chr(i+64)}{j}",end=" ") # ' chr ' conversts to Charcter from Ascii Value(A -> 65 )
    print()
print() 
