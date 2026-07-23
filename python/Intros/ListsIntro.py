# list = Ordered , Mutable Collection that used to store multiple values(multiple Data Types) in a single var .

food=["Pizza","Burgers","Pie","Biryani"] 
# print(food[:]) #Slicing same as Strings 
food[1]="Sooshi"

food.append("Ice Cream") #append will be at End
food.remove("Pie")
food.pop() #remove last element or Given Index Elemnet
food.insert(0,"Cake")
food.sort() #Sort List , .sort(reverse=True) -> for Descending
food.clear() #Clears all Elements in List
food.reverse() #Reverse the List
food.extend([1,2]) #Extends all Items from another List
food.count(1) #Counts Occurences of that Elenmnet
food.index(1) #returns Index of that Element
b=food.copy() #Copy List to NAother

empty=[] #Empty List
nested=[[1,2],[3,4]] #Nested Lists
print(nested[0][1])

print(len(food)) #Return Length of that List
print("Sooshi" in food) #True if Present


for x in nested :
    print(x)
print()

#with INdex using EENumerate
for i,val in enumerate(nested):
    print(f"{i} : {val}")
print()

#List Comprehension (one line Loop)
squares=[x**2 for x in range(1,6)]
print(squares)

#Build in Fucntiions with Lists

print(min(squares),max(squares),sum(squares))