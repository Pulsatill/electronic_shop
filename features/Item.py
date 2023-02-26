
class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, amount, pay_rate=1):
        self.name = name
        self.price = price
        self.amount = amount
        self.total = None
        self.pay_rate = pay_rate
        Item.all.append(self)

    def calculate_total_price(self):
        self.total = self.price * self.amount
        return self.total

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price
