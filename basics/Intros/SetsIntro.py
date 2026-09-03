# set = unordered , mutable collection  of Unique ELemnets .
# Duplicates are automatically Removed
# sets are mutable but elements are Immutable 

fruits = { "Apple" , "Banana" , "Mango"}
nums={1,2,3,4}

empty=set()  #empty Set , must uset set() not {} (thats an empty dict)

#list -> Sey
my_list=[1,2,3]
my_set=set(my_list)
print(my_set)

#Adding and Rempoving
fruits.add("Cherry")
fruits.discard("Mango") #remove(no error if Missing)
fruits.remove("Banana") #remove(KeyError if missing)

##Set Operations
a={1,2,3,4}
b={3,4,5,6}

print(a|b , a.union(b)) #Union
print(a & b , a.intersection(b))
print(a-b,a.difference(b))
print(a^b,) #Symmentric Diff

#Subset or Super Set and disjoint

print({1,2}.issubset(a)) # True
print(a.issuperset({1,2})) # True
print(a.isdisjoint(b)) # True if both sets share no element

# Best Uses : 
# Removing Duplicates form List , fast menembership Testin(in on a set in O(1))
# operations like finding common b/n two Groups 