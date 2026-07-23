t1=(1,2,-4,-1,0,-3,-345,23,-32,54,98)

#Create NEw Tuple with on +ve number 
t2=[]
for x in t1:
    if x>0:
        t2.append(x) #Tuple is Immutable , so it changed to List and later it COnverts
print(tuple(t2))

#Conactinate two Tuples and Sort
l1,l2=list(t1),list(t2)
for i in t2:
    list(t1).append(i)
l1.sort()
print(tuple(l1))

#Unpacking Tupke as (n,*,data)
t=(1,2,3,4,5)
l=list(t)
n=2
for i in l :
    print(f"{n} * {i}")
print()

#Creating tuple of Tuples and sort based on Age
data=(("Dileep",19),
      ("Virat",37),
      ("Ronaldo",42),
      ("Kalyan",54),
      ("Harshith",12))
data_list=list(data)
i=0
for items in data_list:
    data_list[i]=list(data_list[i])
    i+=1
print()
for i in range(0,len(data_list)):
    for j in range(0,len(data_list)-1):
        if data_list[j][1]>data_list[j+1][1]:
            temp=data_list[j]
            data_list[j]=data_list[j+1]
            data_list[j+1]=temp 
i=0
for items in data_list:
    data_list[i]=tuple(data_list[i])
    i+=1
print(tuple(data_list))

