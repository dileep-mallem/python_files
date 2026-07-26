# Can define own Exception by inheriting from Exception .

# Basic custom exception
# class InsufficientFundsError(Exception):
#     """Raised when a withdrawal exceeds the account balance."""
#     pass

# Custom exception with extra data
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field   = field
        self.message = message
        super().__init__(f"[{field}] {message}") 


# Hierarchy of custom exceptions
class AppError(Exception):        # base for all app errors
    pass

class DatabaseError(AppError):    # specific child
    pass

class NetworkError(AppError):     # another child
    pass 


# With Bank Example 
class InsufficientFundsError(Exception): 
    def __init__(self,balance,amount): 
        self.balance=balance
        self.amount=amount
        super().__init__(
            f"Cannot WithDraw ₹{amount} Balance is only ₹{balance}"
        )

class BankAccount :
    def __init__(self,balance=0):
        self.balance=balance 

    def withdraw(self,amount):
        if amount <= 0 :
            raise ValueError("Amount must be Postive")
        if amount > self.balance :
            raise InsufficientFundsError(self.balance,amount)
        self.balance-=amount 
        print(f"WithDraen : ₹{amount} New Balance : {self.balance}")
acc=BankAccount(500)
try :
    acc.withdraw(900)
except InsufficientFundsError as e:
    print(f"Error : {e}")
    print(f"You need ₹{e.amount - e.balance} more.")

    
# When to use custom exceptions: When your code has domain-specific error conditions that built-in 
# exceptions don't express clearly. Names like InsufficientFundsError, InvalidUsernameError, 
# or RateLimitExceeded make code self-documenting and let callers handle errors precisely.