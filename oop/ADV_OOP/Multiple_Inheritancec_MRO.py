# The Diamond Pattern and MRO visual

# Multiple Inheritance and Method Resolution Order (MRO

# MI is an OOP feature iin which a single child class inherits props and methods from tow or more parent classes 
# by sepecyfying them inside parenthesis , sep by comma , 

class parent1:
    pass 
class parent2:
    pass 
class child(parent1,parent2):
    pass 

# Example 
class Employee :
    def employee_details(self):
        print("Employee name : Dileep")
        print("Employee ID : 101")
class Salary :
    def salary_details(self):
        print("Monthly Salary: 50000")

class Manager(Employee,Salary) : 
    def manager_details(self) :
        print("Designation : Project Manager")

# Obj Creattion 
m=Manager()

m.employee_details()
m.salary_details()
m.manager_details()

print("\n")
# Instead of implementing everything inside one enormous class, we can divide functionality into separate classes.
class Walking:
    def walk(self):
        print("Robot is walking")
class Flying:
    def fly(self):
        print("Robot is flying")
class Speaking:
    def speak(self):
        print("Robot is speaking")
class Robot(Walking, Flying, Speaking):
    def activate(self):
        print("Robot activated")
r = Robot()

r.walk()
r.fly()
r.speak()
r.activate()

# uses of MI : Code Reusabilty , Modularity , Extensibity , maintainbilty , Flexibilty 

# What happens when two parent classes contain methods with the same name?
# Then comes MRo(Method resolution Order)
# (MRO) is the order in which Python searches classes to find a method or attribute when an object accesses it.
class Parent1:
    def show(self):
        print("Parent1 method")
class Parent2:
    def show(self):
        print("Parent2 method")
class Child(Parent1, Parent2):
    pass
obj = Child()
obj.show() # Parent 1 Method -> Because the inheritance declaration is: class Child(Parent1, Parent2):
# order is Child , left to right , Depth First (child,p1,p2,obj)

# how to chect MRo n ptyhon
class A :
    pass 
class B : 
    pass 
class C(A,B):
    pass 
print(C.mro())# or print(C.__mro__) -> # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

# mro() is method , returns List retrive MRo ,Returned list can be modified independently
#  __mro__ is atrribute , return tuple , inspect MRo ,Tuple is Immutable 


# // MRO — C3 Linearization — Diamond Problem , generates a consistent linear sequence of classes
# A
# / \
# B C
# \ /
# D ← inherits from both B and C
# If both B and C inherit from A, how does Python decide the order in which to search these classes?
# Question: D() calls A.__init__. Which path? B→A or C→A?
# Without MRO: A.__init__ could run TWICE (once via B, once via C).
# Python's answer: C3 linearization algorithm ensures EVERY class appears
# exactly ONCE in a consistent order.
# D.mro() → [D, B, C, A, object]
# Each class appears exactly once. Left to right, depth first, consistent.

# super() - provides access to the next class in the Method Resolution Order.
# commonly used to call methods defined in parent classes.

# super() does not simply mean "call my immediate parent class."
# Call the next implementation in the current class's MRO.

class Parent : 
    def show(self) : 
        print("Parent Method")
class Child(Parent) : 
    def show(self) : 
        print("Child Method") # Python executes Child.show().

        super().show() # super().show() searches the next class in the MRO.
obj=Child()
obj.show() 

# super() in MI 
class A : 
    def show(self) : 
        print("A")
class B(A) : 
    def show(self) : 
        print("B")
        super().show()
class C(A) : 
    def show(self) : 
        print("C")
        super().show()
class D(B,C) : 
    def show(self):
        print("D")
        super().show()
obj=D()
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
obj.show() # D B A C 

# Cooperative Multiple Inheritance 
# multiple classes work together by calling super() to ensure that each method in the MRO gets an opportunity to execute.
# Instead of explicitly calling parent classes, every participating class delegates to the next class in the MRO.

print("Non Co-operative MI")
class A :
    def show(self) : 
        print("A")
class B(A) : 
    def show(self):
        print("B")
        A.show(self)
class C(A) : 
    def show(self):
        print("C")
        A.show(self)
class D(B,C) : 
    def show(self):
        print("D")
        B.show(self)
        C.show(self)
obj=D()
obj.show() # D B A C A 

# problem : The inheritance chain is manually controlled.,A.show() Twice ,Changes in the class hierarchy can require changes in method calls.
print("\nCooperative Example")
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        super().show()
class C(A):
    def show(self):
        print("C")
        super().show()
class D(B, C):
    def show(self):
        print("D")
        super().show()
obj = D()
obj.show() # DBCA 

