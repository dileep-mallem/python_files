# A closure is a function + a snapshot of its enclosing scope's variables.
#  When an inner function refers to variables from the outer function,
#  Python keeps those variables alive even after the outer function finishes.
# The inner function "closes over" those variables — hence the name closure. 

# A closure is an inner function that uses a variable from the enclosing functio

def make_multiplier(n) : 
    def multiplier(x) : 
        return x*n 
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))              # 10
print(triple(5)) 


# Insided with InreoSpection 

print(double.__code__.co_freevars) # ('n',)
print(double.__closure__) # (<cell at 0x000002294ABC61D0: int object at 0x00007FFB26CDC3C8>,) 
print(double.__closure__[0].cell_contents) # 2

# Changing cap state with nonlocal 

def make_counter() : 
    count=0 
    def step() : 
        nonlocal count 
        count += 1 
        return count 
    return step 
a = make_counter()
b = make_counter()
print(a(), a(), a())          # 1 2 3
print(b()) # 1 ( b has its own cell)

# Mutating not rebinding 
# Calling .append() changes the object a name points to, it does not reassign the name. So no nonlocal is needed for mutable state.

def make_log() : 
    items=[]

    def add(x) : 
        items.append(x)
        return len(items)
    return add 

log = make_log()
print(log("a"), log("b"))     # 1 2

# clousre and OOp (the class Thing) 

def make_account(bal) : 
    def deposit(amount) : 
        nonlocal bal 
        bal += amount 
        return bal 
    def withdraw(amount) : 
        nonlocal bal 
        if amount > bal:
            raise ValueError("insufficient funds")
        bal -= amount
        return bal 
    def get_bal() : 
        return bal 
    return deposit,withdraw,get_bal

deposit, withdraw, get_balance = make_account(100)
deposit(50)
withdraw(30)
print(get_balance())
# print(balance)              # NameError: the state is unreachable from outside 

# classes version 
class Account:
    def __init__(self, balance):
        self._balance = balance           # "private" only by convention
    def deposit(self, amount):
        self._balance += amount
        return self._balance
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        return self._balance
    @property
    def balance(self):
        return self._balance


# The Bridge : A class  __call__ : is a claable obj , the OOP twin of a closure that holds one piece of state. 

class counter : 
    def __init__(self) : 
        self.count=0
    def __call__(self):
        self.count += 1 
        return self.count

c=counter()
print(c(),c())  # 1 2    same behaviour as make_counter()