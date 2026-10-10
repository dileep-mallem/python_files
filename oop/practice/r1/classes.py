# A class i s blu print. and obj is an instance of class . 
# In class , the commeon  are theirt name and age and branch , We can stire thaem useing class without repetive code and we can stor of diff student by usinf diff intsnaces of class .


class BankAccount : 
    bank_name = "PyBank" # Cass VAr : Shared by all Instances 

    def __init__(self, owner : str , balance : float =0.0) : 
        # Instance VAr's : Unique to each obj 
        self.owner=owner 
        self.balance=balance 
        self._history=[] # _ -> private  

    def deposit(self,amount : float) : 
        if amount <= 0 : 
            raise ValueError("Amount must be Positive")

        self.balance+=amount 
        self._history.append(f"+{amount}") # *

    def withdraw(self,amount : float) : 
        if amount> self.balance :
            raise ValueError("Insufficient Balance")
        self.balance-=amount 
        self._history.append(f"-{amount}")

    def __str__(self) : 
        return f"[{self.bank_name}] {self.owner}: {self.balance:.2f}\-"

# Creating Objects (Instances)

acc1=BankAccount("Dileep",22000)
acc2=BankAccount("Jon Snow")

print(acc1,"\n",acc2)

acc1.deposit(7800000)
print(acc1)



acc2.deposit(79800)
acc1.withdraw(880800)

print(acc1._history)
print(acc1.balance)
print(acc2)
print(BankAccount.bank_name)
