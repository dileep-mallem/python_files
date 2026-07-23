#print alphabet
print(f"ASCII 'A' : {ord('A')} Z : {ord('Z')} a:{ord('a')} z :{ord('z')}")

def alphabet(end,start='A'):    
    i=ord(start) 
    j=ord(end)
    for i in range(i,j+1):
        print(chr(i),end=" ")
    print()

alphabet('H')
alphabet('M','C')
alphabet('Z','X')
alphabet('a','S')
print("-------")


n=3
s=ord('A')
for i in range(0,n):
    for space  in range(n-i-1,0,-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print(f"{chr(s)} ",end=" ")
        s+=1
    print()
for i in range(n-1,0,-1):
    for space in range(n-i,0,-1):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(f"{chr(s)} ",end=" ")
        s+=1
    print()
