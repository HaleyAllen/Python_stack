
class Store:
    def __init__(self):
        self.name = "Walbert"
        self.location = "oregon"
        self.chains = 4

    def add_product(self, attribute, amount):
        setattr(Products,attribute, amount)

    def sell_product(self, attribute):
        delattr(Products,attribute)


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

Store.add_product("pad_thai", "$7.99")
Store.add_product("smoothie_mix","$9.99")
Store.add_product("mascara", "$3.99")