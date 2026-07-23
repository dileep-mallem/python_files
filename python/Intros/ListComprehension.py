# A concice way to createlists in Pyhton , compact and easy toread than traditional loops 
# [expression for value in iterable if condition]

doubles = [x**2 for x in range(1,5)]
print(doubles)


fruits = [ "apple", "banana","orange","coconut"]

fruits =[fruit.upper() for fruit in fruits]
print(fruits)

even=[x for x in range(1,101) if x%2==0]
print(even)