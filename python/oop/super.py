# super() -> method used to access methods and attributes of base class
class Car:
    def __init__(self,type):
        self.type=type 

    def start():
        print("Car Started")

class mercedes(Car):
    def __init__(self,name,type):
        self.name=name 
        super().__init__(type)

car1=mercedes("Rolls Royce","Petrol")
car1.start()
print(f"Name : {car1.name} Type :{car1.type}")

