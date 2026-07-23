# tuple = ordered , Immutable coolection 
#           used to group together Related Data(Mutiple Data Type)
# faster than Lists and used for fixed data , can be Used as Dictionary Keys
#Accesion same as Strings and Lists 

student = ("Bro",21,"Male")
for x in student : 
    print(x)
print()

empty=() #empty tuple
no_paren= 1, 2, 3 #parenthesis Options
print(no_paren) #(1,2,3)
print(student)

#Tuple Methods

student.count("Bro")
student.index("Male")

#Convert List <-> Tuple
my_list=list(student)
my_tuple=tuple(my_list)

#Useful with zip()

names = ["Alice","Bob","Charlie"]
scores = [90,85,78]

for name,score in zip(names , scores):
    print(f"{name} : { score}")
print()



