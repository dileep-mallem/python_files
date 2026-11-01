# it is a immutable tuple subclass whose elements can be accesses by 
# both position and by descriptiove filed anme , Useful for lightweight records/objects 

from collections import namedtuple 

Student=namedtuple("Student",["name","age",'dept'])
s=Student("Dileep kumar",20,"Ai/ML")

print(s.name) # Dileep kumar
print(s[1]) # 20 
name,age,dept=s

# imp props 
# Named tuples are immutable, support indexing, unpacking, iteration and tuple-compatible comparisons
# A named tuple can compare equal to an ordinary tuple containing the same values
# They are lightweight records, not general mutable data containers

# Useful named-tuple methods

# _fields: tuple of field names.
# _asdict(): return an ordered mapping/dictionary representation.
# _replace(field=value): return a new instance with selected fields replaced.
# _make(iterable): construct an instance from an iterable
print(s._fields) # ('name', 'age', 'dept')
print(s._asdict()) # {'name': 'Dileep kumar', 'age': 20, 'dept': 'Ai/ML'}
s1=s._replace(name="Muadib")
print(s.name) # Dileep kumar
print(s1.name) # Muadib

s2=s._make(["Dileep kumar",20,"Ai/ML"])
print(s2) # Student(name='Dileep kumar', age=20, dept='Ai/ML')

# typing.namedTuple 
from typing import NamedTuple 
class EvaluationResult(NamedTuple) : 
    accuracy : float 
    precision : float 
    recall: float = 0.0
result=EvaluationResult(0.95,0.93)
print(result.accuracy) # 0.95 

# DataClass vs namedTRuples 
# Use a dataclass for richer data objects with defaults, methods, optional mutability, validation and field customization
# Use a named tuple for a lightweight immutable record that should retain tuple behavior and positional unpacking
# useordinary tuple for simple sequences without named fields