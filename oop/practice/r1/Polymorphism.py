# many Forms 
# THe Smae Method name behaves diffently depending on the obj called on 
# Two : Method Overrising and Duck typing 

class Shape : 
    def area(self) : 
        raise NotImplementedError("Subclass must implement area()")
    def describe(self) : 
        return f"{type(self).__name__} with area {self.area():.2f}"

class Circle(Shape) : 
    def __init__(self,radius) : 
        self.radius=radius 
    def area(self) :
        return 3.14 * self.radius **2 
class Rectangle(Shape) : 
    def __init__(self,w,h) : 
        self.w=w 
        self.h=h 
    def area(self) : 
        return self.w * self.h 
    
class Triangle(Shape) : 
    def __init__(self,base,height) : 
        self.base=base 
        self.height=height 
    # def area(self) : 
    #     return 0.5 * self.base * self.height 

shapes=[Circle(5),Rectangle(4,6),Triangle(3,8)]

for s in shapes : 
    print(s.describe())

# Duck typing: Python doesn't care about the type of an object — only whether it has the method being called. "If it walks like a duck and quacks like a duck, it's a duck." 
# This means any class with an area() method works in the loop above, even without inheriting from Shape.