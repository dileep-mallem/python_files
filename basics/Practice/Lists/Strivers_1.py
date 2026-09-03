#Largest Element 

l=[3,5,4,1,7,8]

# print(max(l)
max=l[0]
for i in l :
    if i> max :
        max =i
print(f"{max} is the largest Lement in an Array ")

#Second LArgest 
#Sort -> two Loops and prnt(l[1])

#Union of Two Arrays 
l1=[2,5,4,6,23,7,1]
l2=[1,2,3,4,5,44,56,5]

u=l1.copy()

for i in l2 :
    if i in u :
        pass 
    else :
        u.append(i)
u.sort()
print(f"Union of {l1} and {l2} is {u}")

#

