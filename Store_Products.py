
class Store:
    def __init__(self):
        self.name = "Walbert"
        self.location = "oregon"
        self.chains = 4

    def add_product(self, attribute, amount):
        setattr(self,attribute, amount)


class Products:
    def __init__(self):
       self.milk = "$3.99"
       self.apple = "$2.99"
       self.eyeLiner = "$5.99"

    def print_info(self):
        print(self.milk)
        print(self.apple)
        print(self.eyeLiner)
        return self

    def update_price_milk(self,amount):
        self.milk = amount

    def update_price_apple(self,amount):
        self.apple = amount

    def update_price_eyeLiner(self,amount):
        self.eyeLiner = amount

Products.add_product()