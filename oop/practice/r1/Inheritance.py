# Inheritance lets the child class or Derived Class to reuse all the attributes and methods of Base class or parent Class , 
# then extend or ovverride them , super() to call parent 

# Single INhertance 

class Animal : 
    def __init__(self,name : str , age : int) : 
        self.name=name 
        self.age=age 
    def speak(self) : 
        return "..."
    def describe(self) : 
        return f"{self.name} (age{self.age}) Says : {self.speak()}"

class Dog(Animal) :  # Dog Inherits from Animal 
    def __init__(self,name,age,breed) : 
        super().__init__(name,age) # call parent constructor 
        self.breed=breed 
    def speak(self) : 
        return " Woof !🐶"

    def fetch(self) :  # New Method specific to Dog 
        return f"{self.name} fetches the ball!"

class Cat(Animal) : 
    # def __init__(self,name,age) : 
    #         super().__init__(name,age) 

    # Doent Need extra COntructor , if same no parametes of Base are Given to Child 
    def speak(self):
        return "Meow ! 🐱"

d=Dog("Bruno",3,"Labrador")
c=Cat("Luna",2)

print(d.speak())
print(d.describe()) #Bruno (age3) Says :  Woof !🐶
print(d.fetch())
print(c.describe()) # Luna (age2) Says : Meow ! 🐱
print(c.speak())
print(isinstance(d,Animal)) # True 
