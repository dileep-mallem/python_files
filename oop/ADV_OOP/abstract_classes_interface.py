# An abstract class defines a contract: "any subclass MUST implement these methods, or Python refuses to instantiate it."
#  Without abstract classes, you'd discover missing method implementations at runtime — too late
# ABCs catch it at object creation time.

from abc import ABC ,abstractmethod 
from typing import Protocol 

# abstract base class 

class Shape(ABC) : 
    """Abstract base for all shapes , Subclass must implement area and perimenter """

    @abstractmethod
    def area(self) :
        """Return the area.""" #  # ... or pass — body is ignored for abstract methods

    @abstractmethod 
    def perimeter(self) : 
        """Retutn the Perimeter"""

    @property 
    @abstractmethod 
    def name (self) : 
        """Shape name - must be an abstract property""" # Concrete method — inherited by all subclasses as-is 

    def describe(self) : 
        return f"{self.name}: area={self.area():.2f},perimeter={self.perimeter():.2f}" # shape() -> typeError -> u cant initiate abstract class Shape <- caught t Creation 

class Circle(Shape) : 
    def __init__(self,r) : 
        self.r=r 
    def area(self):
        return 3.14*self.r**2 
    def perimeter(self):
        return 2*3.14*self.r 
    @property
    def name(self) : 
        return "Circle"

class Rectangle(Shape) : 
    def __init__(self,l,w) : 
        self.l=l 
        self.w=w 
    def area(self):
        return self.l*self.w 
    def perimeter(self):
        return 2*(self.l+self.w) 
    @property
    def name(self) : 
        return "Rectangle"

shapes=[Circle(4),Rectangle(3,5)]
for s in shapes : 
    print(s.describe())

# Circle: area=50.24,perimeter=25.12
# Rectangle: area=15.00,perimeter=16.00

# protocol : structural subtyping(modern alternative) 
# Protocal says : "anything with these methods IS this type"
# no need to Inherit - duck typing with type checking 

class Drawable(Protocol) : 
    def draw(self) : 
        ...
    def area(self):
        ...
class Triangle : # does not inherit Drawable or shape 
    def __init__(self,b,h):
        self.b=b 
        self.h=h 
    def draw(self):
        return "△"
    def area(self) : 
        return 0.5 * self.b * self.h


def render(thing : Drawable) : # type checker accepts Triangle here 
    return f"{thing.draw()} area={thing.area()}"
print(render(Triangle(6,4))) # △ area=12.0  # works — Triangle has draw() and area() 

 # ABC vs Protocol: # ABC: "you must inherit from me and implement X" — explicit contract
 # Protocol: "if you have X, you are this type" — implicit (duck typing)
 # Use ABC for: frameworks, plugin systems, sklearn-style transformers 
 # Use Protocol for: internal code, libraries where you don't control subclasses

