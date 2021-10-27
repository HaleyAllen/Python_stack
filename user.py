
class User:		
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	
    	self.account_balance += amount	
        return self
    # adding the withdrawal method
    def make_withdrawal(self, amount):	
        self.account_balance -= amount	
        return self
    # display balance
    def display_user_balance(self):	
        print("Name;",self.name + ", Balance:",self.account_balance)
        return self
    # transfer money
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


ellen = User("Ellen Merkyl", "ellen@python.com")
monty = User("Monty Python", "monty@python.com")
peter = User("Peter Rabbit", "pter.rabbit@python.com")

ellen.make_deposit(400).make_deposit(900).make_deposit(100).make_withdrawal(800).display_user_balance()

monty.make_deposit(1400).make_deposit(1400).make_withdrawal(300).make_withdrawal(400).display_user_balance()

peter.make_deposit(1400).make_withdrawal(300).make_withdrawal(400).make_withdrawal(400).display_user_balance()

monty.transfer_money(ellen,500).display_user_balance()