# In python , functions are first-class-objs .
# This means a fn is just another value - like int or str 
# It can be stored in var,put in a list or dict , passes aas an arg to another fun , retutned from fn 
# colsures , decorators and call backs are built from thi 

# The test: Can you do X with a function the same way you do it with the integer 42? 
# Assign it: f = 42 → f = my_func? Put in a list: [42] → [my_func]? 
# Pass to a function: g(42) → g(my_func)? 
# If yes for all three, functions are first-class in that language.
#  Python: yes for all three.

# All Four Abilities in a code 

# 1. Store in a variable 

def greet(name : str) : 
    return f"Hello , {name} !"
say_hello=greet # no () - we are string not calling 
print(say_hello('Dileep')) # Same Fn 
print(say_hello.__name__) # greet - its the same obj 

# 3. Put in a data structure 

import math 

ops={"add" : lambda x,y : x+y,"mul":lambda x,y : x*y , "sqrt" : math.sqrt }
# stdlib fun -> also first class 

print(ops["add"](3,4)) # 7
print(ops["sqrt"](16)) # 4.0 

# 3. Pass an argument 

def apply_twice(func,value) : 
    """Apply func to value, then apply func again to the result."""
    return func(func(value))

def double(x) : return x*2 
def square(x) : return x**2

print(apply_twice(double,3)) # 12 double(double(3)) - 2 * 3 * 2 
print(apply_twice(square,2)) # 16 

# 4. Retutn from a fn 

def make_multiplier(n) : 
    def multiplier(x) : 
        return x*n # n comes from outer scope - this is a clousure 
    return multiplier # returning a fn obj 
triple=make_multiplier(3) # triple is now a fun 
print(triple(5)) # 15
print(triple(10)) # 30 
print(type(triple)) # <class 'function'>

# highest Order Functionss and stdlib examples 

# map(func,iterable) - apply func to every varl=iable 
nums=[i for i in range(1,6)]
squared=list(map(lambda x : x**2,nums))
print(squared) # [1, 4, 9, 16, 25] 

# filter(func,iterable) - keep elements where func retutrn True 
even=list(filter(lambda x : x%2==0 ,nums)) 
print(even) # [2,4]

# sorted with key= - sort by a custom functions 
words=["banana","apple","cherry","date"]
print(sorted(words)) # ['apple', 'banana', 'cherry', 'date'] Alphabetical 
print(sorted(words,key=len)) # ['date', 'apple', 'banana', 'cherry'] 
print(sorted(words,key=lambda w : w[-1])) # last char : ['banana', 'apple', 'date', 'cherry']

# Ml Example : sort models by their score 
models=[{"name" : "RF" , "score":0.91}, {"name": "LR", "score": 0.85}, {"name": "SVM", "score": 0.93} ]
best=sorted(models,key=lambda m : m["score"],reverse=True )
print(best[0]["name"]) # SVM 

# functools.reduce - fold a list into a single value
from functools import reduce 

product=reduce(lambda acc , x : acc * x , nums)
print(product) # 120 
