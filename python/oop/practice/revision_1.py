class Book()  : 

    def __init__(self,title : str ,author : str , pages : int ) : 
        self.title=title 
        self.author = author 
        self.pages = pages 
        
    def __str__(self) :
        return f"{self.title} by {self.author} ({self.pages} pages)"
    
    def is_long(self) :
        return True if self.pages > 300 else False  
    
b=Book("Dune","Denis Vinillenue",10781)

print(b) # Dune by Denis Vinillenue (10781 pages) 
print(b.is_long())

# Circle with Property with decorators Only 

class Circle : 
    
    def __init__(self,radius : float) : 
        self._radius = radius # use setter via Property 

    @property
    def radius(self) : 
        return self._radius 

    @radius.setter 
    def radius(self,value : float) : 
        if value < 0 :
            raise ValueError("Cant be Less than Zero !!")
        self._radius = value 

    @property
    def area(self) : 
        return 3.14 * self._radius * self._radius 
    @property
    def circumference(self) : 
        return  2 * 3.14 * self._radius 
    
c = Circle(5)
print(f"Area: {c.area:.2f}")             # Area: 78.54
print(f"Circumference: {c.circumference:.2f}") # Circumference: 31.42
c.radius = 10
print(f"New area: {c.area:.2f}") 




