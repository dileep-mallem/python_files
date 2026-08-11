n=int(input("Enter NUmber : "))

#Traianle 

#First Space 
for i in range(1,n+1):
    for j in range(n-i,-1,-1):
        print(" ",end=" ")
    for i in range(0,2*i-1):
        print("*",end=" ")
    print()
print()

#Inverted Traingle 

for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(2*i-1,0,-1):
        print("*",end=" ")
    print()
print()

#Kite(Diamond)
for i in range(1,n+1):
    for j in range(n-i,-1,-1):
        print(" ",end=" ")
    for i in range(0,2*i-1):
        print("*",end=" ")
    print()
print()
for i in range(n-1,0,-1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for k in range(2*i-1,0,-1):
        print("*",end=" ")
    print()
print()


#Numbers Pyraminds 

# 1 , 0 1 , 1 0 1 , 0 1 0 1 for n=4

for i in range(1,n+1):
    m=1 if i%2!=0 else 0 # odd row No starts with 1 , Even 0 
    for j in range(1,i+1):
        print(m,end=" ")
        if m==1 :
            m=0
        elif m==0 :
            m=1
    print()
print()

#Right angle No Py , Inverted Traingle and Left Tiled Right Angled Pyramd
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(0,2*(n-i)):
        print(" ",end=" ")        
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
print()

#1,2 3 , 4 5 6 for n=3
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()
print()

# A,AB,ABC,ABCD,ABCDE  and its Down Mirror Imgae
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
print()
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
print()

#A,BB,CCC,DDDD
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
print()

#Traingle of A,ABA,ABCBA,ABCDCBA for n=4
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(chr(k+64),end=" ")
    if i>=2:
        for l in range(1,i):
            print(chr(64+l),end=" ")
    print()
print()

#Another with Mid Pont
for i in range(1,n+1):
    mid=(2*i + 1 )//2
    for j in range(n-i,0,-1):
        print(" ",end=" ")
    ch='A'
    for k in range(1,2*i):
        print(ch,end=" ")
        if k<mid :
            ch=chr(ord(ch)+1) #ord(character) -> ASCII
        else : 
            ch=chr(ord(ch)-1)
    print()
print()

#*E,DE,CDE,BCDE,ABCDE 
for i in range(1,n+1):
    start_chr=chr(ord('A')+n-i)
    for j in range(1,i+1):
        print(start_chr,end=" ")
        start_chr=chr(ord(start_chr)+1)
    print()
print()
        

#Space Diamond Rem Starts
for i in range(1,n+1):
    for j in range(n-i,-1,-1):
        print("*",end=" ")
    for k in range(1,2*i-1):
        print(" ",end=" ")
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,n+1-i):
        print("*",end=" ")
    for k in range(2*i-1,1,-1):
        print(" ",end=" ")
    for j in range(0,n-i+1):
        print("*",end=" ")
    print()
print()
    
#*
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        #Computing its Distance from all four bordrs.
        top=i
        bottom=(2*n-2)-i
        left=j
        right=(2*n-2)-j
        #Taking Min for above Four
        min = top 
        if left < top and left < bottom and left < right :
            min=left
        if bottom < top and left > bottom and bottom < right :
            min=bottom
        if right < top and right < bottom and left > right :
            min=right

        #Printing n-minDistance at that Position 
        print(n-min,end="")
    print()
print()

                
                

        



