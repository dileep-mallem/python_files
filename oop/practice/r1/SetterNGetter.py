# Getters and setters let you control how attributes are read and written
# without the user needing to know the internal implementation.

# Tradional and @property way 

# Traditional 

class Temperature : 
    def __init__(self,celcius : float) : 
        self._celcius = celcius  # Protected

    def get_celcius(self) : 
        return self._celcius 

    def set_celcius(self,value: float) : 
        if value < -273.15 : 
            raise ValueError("Temperature below absolute zero!")
        self._celcius=value 

    def get_fahrenheit(self) : 
        return self._celcius * 9/5 + 32 

t=Temperature(25)
print(t.get_celcius(),t.get_fahrenheit())
t.set_celcius(100)
print(t.get_fahrenheit())


# @property DECORATOR , using simple dot . notation

class T : 
    def __init__(self,celcius : float) : 
        self._celcius = celcius 

    @property # getter 
    def celcius(self) : 
         return  self._celcius
    @celcius.setter
    def celcius(self,value):
        self._celcius=value 
        
    @property
    def fahrenheit(self) : 
        return self._celcius * 9/5 + 32 

t=T(25)
print(t.celcius,t.fahrenheit)
t.celcius=100
print(t.celcius)
# t.fahrenheit=80 # Attribute Error (no setter defined)