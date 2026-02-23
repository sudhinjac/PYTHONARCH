from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, accountno, customerName, accountType, balance):
        
        self.accountNo = accountno
        self.customerName = customerName
        self.accountType = accountType
        self.balance = balance
        
    def __str__(self):
        return "Account No: {}\n Customer Name: {}\n Account Type {}\n \
         Balance: {}\n".format(self.accountNo,self.customerName,self.accountType,self.balance)
         
    @abstractmethod
    def withDraw(self,amount): pass

class savingsAccount(Account):
    def withDraw(self,amount):
        if (self.balance - amount < 500):
            raise Exception("Balance Amount is lesser than Rs. 500")
        else:
            self.balance -= amount

class currentAccount(Account):
    
    def withDraw(self,amount):
        self.balance -= amount
        

sa = savingsAccount(101, "sudhin", "Savings", 1000)
print(sa)
amount = float(input("enter the amount: "))
sa.withDraw(amount)
print("Current Balance is : ",sa.balance)


ca = savingsAccount(101, "sudhin", "Savings", 15000)
print(ca)
amount = float(input("enter the amount: "))
ca.withDraw(amount)
print("Current Balance is : ",ca.balance)