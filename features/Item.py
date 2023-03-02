import csv
import os.path


class Item:
    pay_rate = 1
    all = []
    csv_file = os.path.join("items.csv")

    def __init__(self, name, price, amount, pay_rate=1):
        self._name = name
        self.price = price
        self.amount = amount
        self.total = None
        self.pay_rate = pay_rate
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if 0 < len(name) <= 10:
            self._name = name
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self):
        self.total = self.price * self.amount
        return self.total

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        with open(csv_file, "r") as f:
            all2 = []
            file_read = csv.DictReader(f)
            for i in file_read:
                name = i["name"]
                price = i["price"]
                amount = i["quantity"]
                all2.append(cls(name, price, amount))
            cls.all = all2
            return cls.all

    @staticmethod
    def is_integer(value):
        if isinstance(value, int):
            return True
        if isinstance(value, float):
            return value.is_integer()
        else:
            return False
