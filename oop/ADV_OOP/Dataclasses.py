# Data Class : class primarly intended to store stuctured Dats . 
# the @dataclass decorator 

from dataclasses import dataclass 

@dataclass  # python calss , include methods __init__,__repr__,and __eq__ 
class Student :  # Standard Python object heap allocation (Reference type). 
    name : str 
    age : int 
    dept : str 
s1=Student('Dileep',20,'AIML')
s2=Student('Ojas',35,'Gansta')

print(s1) # Student(name='Dileep', age=20, dept='AIML')
print(s1==s2) # False 

# Type annotations are not runtime validation 
# For validation, add explicit checks (often in __post_init__) or use a validation
# library such as Pydantic

# Generated Methods 
# By default, @dataclass generates __init__, __repr__ and __eq__
# Ordering methods are generated only when order=True.
# Hash generation depends on eq, frozen and unsafe_hash setting

# Important Decorator Options 

# init=True: generate the constructor.
# repr=True: generate a readable representation.
# eq=True: generate equality comparison.
# order=False: do not generate ordering methods by default.
# frozen=False: instances are mutable by default.
# slots=False: use normal instance storage by default.
# unsafe_hash=False: do not force hash generation.

# Frozen Data Classes 
# @dataclass(frozen=True) prevents ordinary reassignment of fields after initialization. 
# It is useful for configuration objects and value-like records. 
# It provides shallow immutability: a list or dictionary stored in a field can still have its contents mutated.

# Ordering 
# @dataclass(order=True) generates comparison methods. 
#  Fields are compared lexicographically in declaration order. Choose field order carefully; 
# use compare=False for fields that should not participate in comparisons

# Slots 
# @dataclass(slots=True) creates slot-based attributes,
# often reducing per-instance memory overhead and preventing arbitrary new attributes
# It can be useful when creating many instances. 
# Measure performance and memory in the application 


# Defaults and Deault Factory 
# Immutable defaults can be supplied directly. 
# For mutable defaults such as lists, dictionaries and sets, use field(default_factory=list) to avoid shared mutable defaults.

from dataclasses import field
@dataclass
class Student : 
    name : str 
    subjects : list[str] = field(default_factory=list)

a=Student("Dileep")
b=Student("Ojas",["Python","Java"])
a.subjects.append("ML")
print(a.subjects) # ['ML']
print(b) # Student(name='Ojas', subjects=['Python', 'Java']) 