# A decorator is a fn that takes a fn as input , adds behaviour and returns a new (enhanced) fn

# The @ syntax  sugar: @decorator above a function is exactly func = decorator(func) — nothing more. 
# Every complexity of decorators comes from cleverness in what the decorator does, not from any special magic.

# * original fn - decorator(adds addinal behaviou) -> Enhanced Function 

def greet() : 
    print("Hello gang !!")

def my_decorator(func) : 
    def wrapper() : 
        print("Before Function Execution") 
        func()
        print("After Function Execution")

    return wrapper

greet=my_decorator(greet) # apply the decorator manually 
greet()
# Before Function Execution
# Hello gang !!
# After Function Execution

# The @decorator syntax 
def my_decorator(func):
    def wrapper():
        print("Before execution")
        func()
        print("After execution")
    return wrapper

@my_decorator # eq to greet=my_decorator(greet)
def greet():
    print("Hello, Python!") 
greet()
# Before execution
# Hello, Python!
# After execution

#** The decorator expression is evaluated when the function is defined, not every time the decorated function is called.

# argument Function Decorators 
# solution *args , **kwargs 
print("\nArgument Function Decorator")
def my_decorator(func) : 
    def wrapper(*args,**kwargs) : 
        print("before Execution")
        result=func(*args,**kwargs)
        print("After Execution")
        return result 
    return wrapper 
@my_decorator 
def add(a,b) : 
    return a+b 
@my_decorator
def greet(name: str) : 
    print(f"Hello {name}")

greet("Dileep")
result=add(10,20)
print(result)
# before Execution
# Hello Dileep
# After Execution
# before Execution
# After Execution
# 30

# *args	Collects positional arguments into a tuple 
# **kwargs	Collects keyword arguments into a dictionary

# functools.wraps 
def my_decorator(func) : 
    def wrapper(*args,**kwargs) : 
        return func(*args,**kwargs)
    return wrapper 
@my_decorator
def greet() : 
    """This Function Greets the user"""
    print('Hello!')
print(greet.__name__) # wrapper 
print(greet.__doc__) # None

# Our decorated function has lost its original metadata.
# Originally, the function was called greet. But after decoration, the variable greet refers to wrapper.
# Affets Debugging , Documentation , Introspection , Testing and Frame Behaviour 
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def greet():
    """This function greets the user."""
    print("Hello!")
print(greet.__name__)
print(greet.__doc__)
# greet
# This function greets the user.
# @wraps(func) preserve , __name__,__doc__,__module__,_-anotations__,__wrapped__ 


# Real Worls Decorator Applications 
print("\nReal Worls Decorator Applications\n")
# Logging Decorator 

# Imagine you have multiple functions in an ML application.
# You want to know:
# - Which function started?
# - Which function completed?
# - What arguments were passed?
# - How long did execution take?
# Instead of writing logging statements repeatedly, we create Decorartor.

from functools import wraps
import logging 

logging.basicConfig(level=logging.INFO)

def log_execution(func) : 
    @wraps(func)
    def wrapper(*args,**kwargs) : 
        logging.info(
             "Executing %s",func.__name__
         )
        result=func(*args,**kwargs)

        logging.info(
            "Completed %s " , func.__name__
        )

        return result 
    return wrapper
@log_execution
def train_model() : 
    print("Model Training ")
train_model()
# INFO:root:Executing train_model
# Model Training 
# INFO:root:Completed train_model

# Timing Decorator
print("\nTiming Decorator") 
import time 

def execution_time(func) : 
    @wraps(func)
    def wrapper(*args,**kwargs) : 
        start=time.perf_counter() # Performance counter for benchmarking.
        result=func(*args,**kwargs) 
        end=time.perf_counter()

        print(
            f"{func.__name__} took "
            f"{end-start:.6f} seconds"
        )

        return result 
    return wrapper 
@execution_time
def calculate() : 
    total=0 
    for i in range(1000000) : 
        total+=i 
    return total 
calculate() # calculate took 0.022361 seconds 

# time.perf_counter() designed for measuring short-duration time intervals and is generally more appropriate for benchmarking than time.time()

# Autheniticaation Decorator 
print("\nAutheniticaation Decorator ")
def authenticate(func) : 
    @wraps(func) 
    def wrapper(user,*args,**kwargs) : 
        if not user.get("authenticated") : 
            print("Acces Denied")
            return None 
        return func(user,*args,**kwargs)
    return wrapper
@authenticate 
def dashboard(user) : 
    print(f'Welcome {user['name']}')

user1={
    "name":"Dileep Kumar",
    "authenticated":True
}
user2={
    "name":"'Muadib",
    "authenticated":False
}
dashboard(user1)
dashboard(user2)
# Autheniticaation Decorator 
# Welcome Dileep Kumar
# Acces Denied

