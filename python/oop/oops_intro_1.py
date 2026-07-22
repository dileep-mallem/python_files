#procedural -> Functional -> OOP(to decrese Reductancy and Incearse Reusability  , to map with Real worrld Scenarios)

#Object -> combination/consists of Varibles(Attributes) and methods(Functions)
#Class -> Class is Blue PRint for Creating Objects

#Creating Class
class Student :
    name = "Dileep Kumar"
    age=19
    cgpa=9.85 

#Creating Object(Instance)
s1=Student()
print(s1,s1.name,s1.age,s1.cgpa)


#Constructor (__init__) -> All classes have a fn called __init__() , which is always exceuted when class is being initiated 

class car :

    x=1010 #Class Attributes(Same for every Object)

    #Default Constructors
    def __init__(self):
        print("Creating a Car Constrcutor")
    
    #Parameterized Constructors
    def __init__(self,fullname,model) : # must always gives atleast one argument (self or other name) , self is ref to current instance of class and used to acces varibles in that class
        self.name=fullname  #Instance Atrribute (Varies for each Object Created )
        self.model=model
        print(self.name,self.model)
c1=car("Mercedes",7777) #calls the Class 
c1=car("BMW",987)


#Class and Instance Attributes , Methods
# n=int(input("Enter No of Students Dta you Have to Enter : "))
n=0

class student :
    college = "RGUKT RKV"
    name = "anonymous"

    def __init__(self,name,branch,marks):
        self.name=name  #Obj Attr > class Attr
        self.branch=branch
        self.marks=marks

    def display(k): #Methods 
        print(f"NAme : {k.name} Branch : {k.branch}  Avg : {sum(k.marks)/3}")

    @staticmethod 
    def clg():
        print("Welcome")
    

for i in range(n):
    name=input("Enter First name : ")
    branch=input("Enter First Branch : ")
    ci=student(name,branch,[56,98,70]) # Saves Data as one Obj 
for i in range(n):
    student.display(ci) #Display Data

#Static Methods -> Which dont Use self par , work at class level
#Abstraction -> Hiding the Implementation details of class and Only Showing the Essentail Features to the User 

class Car :
    def __init__(self):
        self.acc=False 
        self.brk=False
        self.clutch=False 
    def start(self):
        self.clutch=True 
        self.acc=True 
        print("Car Started")
car1=Car()
car1.start()

#Encapsulation -> Wrapping data and functions into Single Unit (object)

class Account : 
    def __init__(self,bal,acc):
        self.balance=bal 
        self.acc_no=acc 

    #debit Method 
    def debit(self,amount) :
        if self.balance < amount :
            print("Not Enough Balance")
        else :
            self.balance -= amount
            print("Rs.",amount," was Debited")
            print("Total Balance : ",self.balance)

    def credit(self,amount) :
            self.balance += amount
            print("Rs.",amount," was Credited")
            print("Total Balance : ",self.balance)

    def get_balance(self):
        return self.balance


acc1=Account(10000,101)
acc1.debit(100000)
acc1.credit(5000)
acc1.credit(900000)
acc1.debit(400000)
print(acc1.get_balance())


    



