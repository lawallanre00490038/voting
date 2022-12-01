import random
import datetime as dt


# baseclass
class BasicAccount:
    acNumber = 0
    def __init__(self, name):
        self.name = name
        self.balance = float(0)
        self.acNum = BasicAccount.acNumber
        self.cardNum = "".join([str(random.randrange(0, 9, 1)) for i in range(16)])
        self.cardExp = dt.date.today().month,int(str(dt.date.today().year)[2:])
        BasicAccount.acNumber += 1
        
    def __str__(self):
        return f"Owner: {self.name} \nBalance: £{self.balance}"
    
    def deposit(self, amount):
        amount = float(amount)
        if amount < 0:
            return ("Your amount should be greater than 0")
        self.balance += float(amount)
        
    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance}")
        else:
            print(f"Can not withdraw £{self.balance}")
            
    def getAvailableBalance(self):
        return(float(self.balance))
    
    def getBalance(self):
        if self.balance < 0:
            return (f"£-{float(self.balance)}")
        return(f"£{float(self.balance)}")
    
    def PrintBalance(self):
        return f"Name: {self.name} Account Number: \
            {float(self.acNum)} Balance: £{float(self.balance)}"
    
    def getName(self):
        return self.name
    
    def getAcNum(self):
        return(str(self.acNum))
    
    def issueNewCard(self):
        self.cardNum = str(random.randint(10**15,(10**16)-1))
        today = dt.date.today()
        self.cardExp = today.month,int(str(today.year+3)[2:])
        print(f"The card number is {self.cardNum} with an expiry date of {self.cardExp}".format(self=self))

    def closeAccount(self):
        self.withdraw(0)
        return True
    
    
    
class PremiumAccount(BasicAccount):
    def __init__(self,name, overdraftLimit = 0.0):
        super().__init__(name)
        self.overdraft = True
        self.overdraftLimit = overdraftLimit
        self.initialOverdraft = 0.0
        
    def withdraw(self, amount):
        if amount > (self.balance + self.overdraftLimit):
            return(f"Can not withdraw £{amount}")
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance = float(self.balance + self.overdraftLimit) - float(amount)
            self.overdraftLimit = self.balance
            self.balance = 0.0
        print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance}")
        
    def setOverDraftLimit(self, newLimit):
        self.initialOverdraft = float(newLimit)
        self.overdraftLimit = float(newLimit)

    def getAvailableBalance(self):
        return float(self.balance + self.overdraftLimit)

    def printBalance(self):
        if self.overdraft:
            print(f"Your Balance: {self.balance} and Your remaining Overdraft: {self.overdraftLimit}")
        else: 
            print(f"Your Balance: {self.balance} and you have no more overdraft")
    
    def closeAccount(self):
        if self.getAvailableBalance() < self.initialOverdraft:
            print(f"Can not close account due to customer being overdrawn by £{(self.initialOverdraft - self.overdraftLimit)}")
            return False
        self.withdraw(0)
        return True

    def __str__(self):
        return f"Owner: {self.name} \nBalance: £{self.balance} with Overdraft limit: £{self.overdraftLimit}"
    

A = PremiumAccount("lanre")
A.deposit(5000)
A.setOverDraftLimit(10000)
print(A)
print(A.withdraw(13000))
print(A)
print(A.closeAccount())
print(A.cardNum)
