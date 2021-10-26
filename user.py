
class User:		
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	
    	self.account_balance += amount	
    # adding the withdrawal method
    def make_withdrawal(self, amount):	
        self.account_balance -= amount	
    # display balance
    def display_user_balance(self):	
        return "User: "+self.name+", Balance: "+self.account_balance
    # transfer money
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


ellen = User("Ellen Merkyl", "ellen@python.com")
monty = User("Monty Python", "monty@python.com")
peter = User("Peter Rabbit", "pter.rabbit@python.com")
print(ellen.name)	
print(monty.name)	
print(peter.name)	

ellen.make_deposit(400)
ellen.make_deposit(900)
ellen.make_deposit(100)
ellen.make_withdrawal(800)

print(ellen.account_balance)

monty.make_deposit(1400)
monty.make_deposit(1400)
monty.make_withdrawal(300)
monty.make_withdrawal(400)

print(monty.account_balance)

peter.make_deposit(1400)
peter.make_withdrawal(300)
peter.make_withdrawal(400)
peter.make_withdrawal(400)

print(peter.account_balance)

monty.transfer_money(ellen,500)

print(monty.account_balance)
print(ellen.account_balance)