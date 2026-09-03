# *args = allows you to pass multiple non-key args
# **kwargs = allows you to pass multiple keyword args
#           * unpacking  operator 

def add(a,b):
    return a+b
print(add(2,3))

def sum(*args): #parameter name can vary
    print(type(args)) #tuple
    total=0
    for arg in args:
        total+=arg
    return total
print(sum(1,2,3)) #6

def display_name(*args):
    for arg in args :
        print(arg,end=" ")
display_name("Dileep","Kumar","MAllem","I")
print()

#**kwargs
def print_address(**kwargs):
    print(type(kwargs)) #dictionary

    for key,value in kwargs.items():
        print(f"{key} : {value}")
print_address(street="Rajampet",
              city="Kadapa",
              state="AP",
              zip="516115")



