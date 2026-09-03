# A class method is bound to the class & recesives the class as an implicity of Argument 

# Note : static method can't access or modify cass state and generally foor utility 

class Person:
    name="Anonymous"
    age=21

    def changeName(self,name):
        # self.name=name ->It creats seprated name var for object not for class 
        #To chane class name :
        # 1.Person.name=name 
        self.__class__.name=name 

    @classmethod
    def changeAge(cls,age):
        cls.age=age
    

p1=Person()
p1.changeName("DIleep")
print(p1.name)
print(Person.name)
p1.changeAge(20)
print(p1.age,Person.age) #20 20
