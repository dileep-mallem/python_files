import math
class Circle :
    def __init__(self,rad):
        self.radius =rad 

    def area(self):
        return math.pi * (self.radius) *(self.radius)
    
    def perimeter(self):
        return 2 * 3.14 * (self.radius)

c1=Circle(2.5)
print(f" Area : {c1.area()} Perimeter : {c1.perimeter()}")

print("----------")

class Employee :
    def __init__(self , role , dept , salary):
        self.role=role
        self.dept=dept 
        self.salary=salary 
    def showDetails(self):
        print(self.role,self.dept,self.salary) 

class Engineer(Employee):
    def __init__(self,name,age):
        self.age=age 
        self.name=name 
        super().__init__("Enginner","IT",700000)
        
    # def showDetails(self):
    #         print(self.name,self.age,self.role,self.dept,self.salary) 
e1=Employee("Google CEO","CSE",8000000000000)
e1.showDetails()
e2=Engineer("Dileep",21)
e2.showDetails()

print("----------")

class Order :

    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,o2): #GreaterThan
        return self.price > o2.price
    
o1=Order("Chips",100)
o2=Order("Tea",75)

print(o1 > o2)