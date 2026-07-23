list1=["1.","2.","3.","4."]
list2=["Dileep","Virat","Ronaldo","Pawan Kalyan"]
i=0
#Merge 2 list
for items in list2:
    list1.append(list2[i])
    i+=1
print()
print(list1)

#sort list1
list1.sort()
print(list1)
#Return Even Numbers in List throgh List COmprehention
list=[1,2,3,4,5,6,7,8,9,0]
even=[x for x in list if x %2==0 ]
print(even)

#Sencond Largest Number without .sort()
numbers=[12,32,4,3,54,6,5,2,45]
for i in range(0,len(numbers)):
    for j in range(0,len(numbers)-1):
        if numbers[j]>numbers[j+1]:
            temp=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=temp 
print(numbers)
