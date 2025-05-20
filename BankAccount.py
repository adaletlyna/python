class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.1, balance=0): #We use default parameters because we want to allow the user to optionally pass in their own values
        self.int_rate= int_rate                   #if I want to always assign a specific value internally	Set it inside __init__(like in the previous assignment )
        self.balance= balance
    def deposit(self, amount):
        self.balance+=amount
        print("your balance now is: ",self.balance)
        return self

    def withdraw(self, amount):
        if self.balance<amount:
            print("unsufficient funds: charging a $5 fee")
            self.balance-= 5
            return self
        self.balance-= amount
        return self

    def display_account_info(self):
        print("Balance:",self.balance)
        return self

    def yield_interest(self):
        if self.balance>0:
            interest=self.balance*self.int_rate
            self.balance+=interest
            print("balance+Interest= ", self.balance)
        return self

account1= BankAccount()
print(account1)
account1.deposit(100).withdraw(20).display_account_info().yield_interest()

