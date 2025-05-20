class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.1, balance=0): #We use default parameters because we want to allow the user to optionally pass in their own values
        self.int_rate= int_rate                   #if I want to always assign a specific value internally	Set it inside __init__(like in the previous assignment )
        self.balance= balance
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if self.balance<amount:
            print("unsufficient funds: charging a $5 fee")
            self.balance-= 5
            return self
        self.balance-= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

class User:

    def __init__(self,name,email):
        self.name= name
        self.email= email
        self.accounts={'account1':BankAccount(0.1,0),'account2':BankAccount(0.11,300)}
        
    def make_deposit(self,amount,account):
        self.accounts[account].deposit(amount)
        print(f"{self.name}'s balance in {account} is now: {self.accounts[account].balance}")
        return self

    def make_withdrawal(self,amount,account):
        self.accounts[account].withdraw(amount)
        return self

    def display_user_balance(self,account):
        print(f"{self.name}'s Account Balance:")
        self.accounts[account].display_account_info()
        return self
    def transfer_money(self,sender_account,amount,other_user,receiver_account):
        
        self.accounts[sender_account].withdraw(amount)
        other_user.accounts[receiver_account].deposit(amount)
        print(f"{self.name} transferred ${amount} from {sender_account} to {other_user.name}'s {receiver_account}")
        return self
  

user1=User("lyna","lyna@gmail.com")
user2=User("iheb","iheb@gmail.com")
user1.make_deposit(500,'account1').make_withdrawal(200,'account1').display_user_balance('account1').transfer_money('account1',100,user2,'account2')
