# BankError (Base) -> InsufficientFundsError and InvalidAmountError. are childs 

class BankError(Exception):
    "Bank Error"
    pass
    
class InsufficientFundsError(BankError):
    def __init__(self,balance):
        self.balance=balance 
        super().__init__(
            f"Not Enough Balance (Your Balance : {self.balance})"
        )
class InvalidAmountError(BankError) :
    def __init__(self,amount):
        self.amnt=amount 
        super().__init__(
            f"Creadit Amount must be Positive"
        )

class BankAccount :
    def __init__(self,balance=0): # if nothings Given ==0 
        if balance < 0 :
            raise InvalidAmountError("Initial mustr be >=0")
        self.balance=balance 

    def credit(self,amount):
        
        if amount <= 0 : 
            raise InvalidAmountError(amount)
        self.balance+=amount
        print("Credited : ",amount," New Balance : ",self.balance)
    def withDraw(self,amount):
        if amount <= 0 : 
            raise InvalidAmountError(amount)
        if amount > self.balance :
            raise InsufficientFundsError(self.balance)
        self.balance-=amount 
        print("WithDrawn : ",amount," New Balance : ",self.balance)
    def showBalance(self):
        print("Balance : ",self.balance) 
acc=BankAccount(1000)
try : 
    acc.withDraw(900)
except InsufficientFundsError as e :
    print("Eroor : ",e)
except InvalidAmountError as i :
    print("Error : ",i)
finally:
    print("Practiced Custom Exceptions !!")
