# Iterables = An object/collection that can return its element one at a time 
#               allowing it to be iterated over in a loop


numbers =[ 1,2,3,4,5]

for i in reversed(numbers):
    print(i,end=" - ")
print()

fruits = {"apple", "orange" , "banana" , "coconut"}

for fruit in fruits :
    print(fruit)