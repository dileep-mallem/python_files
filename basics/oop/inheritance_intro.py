#one class(child/derived) derived the props of another class (parent/base)

#Single Inhertance 
class Surname :
    sur_name = "Mallem"
    mother_name="Reddamma"

class child(Surname):
    def __init__(self,name):
        self.name=name
        
p1=child("Dileep Kumar")
p2=child("Raghu")

print(p1.sur_name,p1.name,"Mother : ",p1.mother_name)

#Multi-level Inheritance (A->b->c)
class Car :
    def start(self):
        print("Car Started...")
    def stop(self):
        print("Car Stoppped !!")

class TATA(Car):
    color="White"

    def __init__(self,name):
        self.car_name=name 

class model(TATA):

    def __init__(self,car_name,model):
        self.model=model 
        super().__init__(car_name)

m1=model("Mercedes","!@#$")

print(m1.car_name,m1.model,m1.color)

#Multiple Inheritance (One Derived class inherit pops and methods from multiple class)
class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to class B"
class C(A,B) :
    varC="Welcome to class C"
c1=C()

print(c1.varA)
print(c1.varB)
print(c1.varC)





