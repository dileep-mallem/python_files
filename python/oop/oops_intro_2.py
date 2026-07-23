# del KEy word -> used to clear object props ot itself 
# class Student :
#     def __init__(self,name):
#         self.name=name 
# s1=Student("Dileep")
# print(s1.name)
# del s1.name 
# print(s1.name) -> Atrribut Error 

#Private attributes & methods -> only accesiblt within the class , self.__name  -> private


class Person:
    __name="Anonymous"

    def __hello(self):
        print("HEllo Person!")

    def welcome(self):
        self.__hello()

p1=Person()
#print(p1.__hello()) #Attrinutr Error
print(p1.welcome())



