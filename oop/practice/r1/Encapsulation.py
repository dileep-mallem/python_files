# Meand Controlling which can be accessed the intenal state of onj .
# Python usus Naming Conventions to signal intent 

# No _ -> public (Anyone can Use it) , accesible from outside 
# Single _ -> protected, yes ( COnvention only)
# Double __ -> Private , Not directly accesed from Outside , use getter and setter to accces 


class Student : 
    def __init__(self,name : str , grade ) : 
        self.name=name 
        self._grade = grade # protected(convention)
        self.__id=id(self) # private(name-mangled)

    def get_grade(self) : 
        return self._grade

    def set_grade(self,new_grade) : 
        if 0<=new_grade<=100 : 
            self._grade=new_grade
        else : 
            raise ValueError("Grade must be 0-100")


s=Student("Dileep",85)
print(s.name,s._grade)
print(s.get_grade()) # 85
s.set_grade(100)
print(s.get_grade()) # 100

# print(s.__id) -> AttributeError: 'Student' object has no attribute '__id'
# print(s._Student__id) # 135144266907600 (works via name mangling , Dont Do this )