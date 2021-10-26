
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
        return"User: "+self.name+", Balance: "+self.account_balance
    # transfer money
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


ellen = User("Ellen Merkyl", "ellen@python.com")
monty = User("Monty Python", "monty@python.com")
peter = User("Peter Rabbit", "pter.rabbit@python.com")

ellen.make_deposit(400).make_deposit(900).make_deposit(100).make_withdrawal(800)

print(ellen.account_balance)

monty.make_deposit(1400).make_deposit(1400).make_withdrawal(300).make_withdrawal(400)

print(monty.account_balance)


peter.make_deposit(1400).make_withdrawal(300).make_withdrawal(400).make_withdrawal(400)

print(peter.account_balance)


monty.transfer_money(ellen,500)

print(ellen.account_balance)
print(monty.account_balance)