# Short for Double UnderScore , are speacial methods like __init__ th   at
# Python call automatically in specific situations . They let your custom 
# classes behave like built-in-types -- supporting len(),print(),+,== and more .


class Student : 
    def __init__(self,name,marks) :  # Constructor — called when an object is created. Sets up initial state.
        self.name=name 
        self.marks=marks 

    def __str__(self) : # prints
        avg=sum(self.marks)/len(self.marks) 
        return f" Student :  {self.name} , avg= {avg:.1f}"

    def __repr__(self) : # Developer-readable representation. Should show how to recreate the object. 
        return f"Student (name={self.name!r}, marks={self.marks!r})"

    def __len__(self) : # return len(obj)
        return len(self.marks)

    def __eq__(self,other) : # equality
        return self.name == other.name 

    def __lt__(self,other) : # compare
        return sum(self.marks) < sum(other.marks)
    def __add__(self,other) : 
        return Student(f"{self.name}&{other.name}", self.marks + other.marks)

    def __contains__(self, mark):
        # 90 in student → did they score 90?
        return mark in self.marks

    def __bool__(self):
        # if student: → True if they have at least one mark
        return len(self.marks) > 0


# Sample Practice 
a = Student("Arjun", [85, 90, 92])
b = Student("Priya", [78, 95, 88])
c = Student("Arjun", [85, 90, 92])

print(a) 
print(repr(a))
print(len(a))
print(a==c) 
print(a==b)
print(a<b)
print(90 in a)
print(bool(a))

comb=a+b 
print(comb) #  Student :  Arjun&Priya , avg= 88.0

# Sort a list of students by average — uses __lt__
roster = [b, a, Student("Ravi", [70, 65, 80])]
print(sorted(roster))
# [Student (name='Ravi', marks=[70, 65, 80]), Student (name='Priya', marks=[78, 95, 88]), Student (name='Arjun', marks=[85, 90, 92])]