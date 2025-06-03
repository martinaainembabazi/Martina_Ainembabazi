class BankAccount:
    def __init__ (self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited {amount}and the balance is now {self.balance}")        


    def withdraw(self,amount):
        if amount >= self.balance:
         self.balance-=amount
         print(f"Withdrew {amount}and the balance is now {self.balance}")  
        else:
         print("Insufficient funds") 

    def display_balance(self):
         print(f"The account {self.account_number} has a balance of {self.balance} ")  

 #subclass Savings account
class SavingsAccount(BankAccount):
   def __init__(self, account_number, balance,interest_rate):
      super().__init__(account_number, balance)  
      self.interest_rate=interest_rate


   def add_interest_rate(self):
      interest=self.balance*self.interest_rate     
      self_balance+=interest
      print(f"the interest of {interest}has been added and the new balance is {self.balance}")    



class CurrentAccount(BankAccount):
   def __init__(self, account_number, balance,overdraft_limit):
      super().__init__(account_number, balance) 
      self.overdraft_limit=overdraft_limit

      #override withdraw method to allow overdraft
      def withdraw(self,amount):
        if amount <= self.balance + self.overdraft_limit:
          self.balance-=amount
          print(f"Current account is ")  
        else:
         print("You have exceeded the overdraft limit")



saving = SavingsAccount("ACC289000",200000,5)         
current=CurrentAccount("CUR27893749",400000,10)


saving.display_balance()
saving.add_interest_rate()
saving.withdraw(10000)


current.display_balance()
current.withdraw(30000)
current.withdraw(2000)