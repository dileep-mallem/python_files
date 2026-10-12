# A multi-account banking system showcasing all four OOP pillars. 
# Account is the base; SavingsAccount and CurrentAccount inherit from it. 
# Balance is protected via @property with validation.


class Account : 
    bank_name="OOP Bank"

    def __init__(self,owner : str , balance : float=0.0) : 
        self.owner=owner 
        self._balance=balance 
        self._history=[]

    @property
    def balance(self) : 
        return self._balance 

    @balance.setter 
    def balance(self,value: float): 
        if value < 0 :
            raise ValueError("Balance Cannot go Negative")
        self._balance=value 

    def deposit(self,amount : float) : 
        if amount <=0 : 
            raise ValueError("Deposit must be Positive")
        self._balance+=amount 
        self._history.append(f"+{amount}")
        print(f" Deposited {amount} \-. New Balance: {self._balance}\-")

    def withdraw(self,amount) : 
        raise NotImplementedError   # subclass must implement 

    def __str__(self) : 
        return f"[{self.bank_name}] {self.owner} -- {self._balance}\-"


class SavingAccount(Account) : 
    MIN_BALANCE=1000 

    def __init__(self,owner,balance=1000.0,interest_rate=0.04) : 
        super().__init__(owner,balance)
        self._interest_rate=interest_rate

    @property
    def interest_rate(self) : 
        return self._interest_rate 

    @interest_rate.setter 
    def interest_rate(self,new_rate) : 
        if not(0<new_rate<1) : 
            raise ValueError("Rate Must be between 0 and 1 ")
        self._interest_rate=new_rate 

    def withdraw(self,amount) : 
        if self._balance - amount < self.MIN_BALANCE : 
            raise ValueError(f"Must Maintain {self.MIN_BALANCE}\- minimum")
        self._balance -= amount 
        self._history.append(f"-{amount}")
        print(f" Withdraw {amount}\- . New Balance {self._balance}")

    def apply_interest(self) : 
        interest=round(self._balance * self._interest_rate , 2)

        self._balance+=interest 
        self._history.append(f"INT +{interest}\- {self._interest_rate*100}%")
        print(f"✔ Interest applied: ₹{interest}")


class CurrentAccount(Account) : 
    def __init__(self,owner,balance=0.0,limit=5000) : 
        super().__init__(owner,balance)
        self._limit=limit 
    def withdraw(self,amount) : 
        if amount > self._balance + self._limit : 
            raise ValueError("Value Exceeded")
        self._balance-=amount 
        self._history.append(f"-₹{amount}")
        print(f"✔Withdrew {amount}\-. Balance:{self._balance}\-")

# Demo 
print("--BankingSystem Demo--")

s=SavingAccount("Dileep Kumar",10000)
s.deposit(2000)
s.withdraw(1000)
s.apply_interest()

print("\n")
c=CurrentAccount("Sreenth",2000,3000)

c.deposit(500)
c.withdraw(4500) # uses limit 

# poly 
accounts=[s,c]
for acc in accounts : 
    print(acc)