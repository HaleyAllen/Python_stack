
class BankAccount:

    def __init__(self, int_rate, balance):
        self.rate= int_rate
        self.account_balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.account_balance += amount	
        return self
    def withdraw(self, amount):
        self.account_balance -= amount	
        return self
    def account_info(self):
        print("Balance:", self.account_balance,"Interest Rate:", self.rate)
        return self
    def yield_interest(self):
        interest = self.account_balance * self.rate
        self.account_balance += interest
        return self

class User:		
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account=BankAccount(int_rate=0.01, balance=0)
    # display balance
    def display_user_balance(self):	
        print("Name;",self.name + ", Balance:",self.account_balance)
        return self
    # transfer money
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

chris=User("Christian Allen", "email@email.com")
haley=User("Haley Allen", "email@email.com")

chris = BankAccount(0.01, 1400)
haley = BankAccount(0.03, 2000)

chris.deposit(400).deposit(900).deposit(100).withdraw(800).yield_interest().account_info()

haley.deposit(4000).deposit(9000).withdraw(200).withdraw(400).withdraw(300).withdraw(600).yield_interest().account_info()