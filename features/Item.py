import csv
import os.path

from features.InstantiateCSVError import InstantiateCSVError


csv_file = os.path.join("items.csv")


class Item:
    pay_rate = 1
    all = []

    def __init__(self, name, price, amount, pay_rate=1):
        if 0 < len(name) <= 20:
            self._name = name
        else:
            raise AttributeError("Длина наименования товара превышает 20 символов.")
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
        if 0 < len(name) <= 20:
            self._name = name
        else:
            raise AttributeError("Длина наименования товара превышает 20 символов.")

    def calculate_total_price(self):
        self.total = self.price * self.amount
        return self.total

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        try:
            with open(csv_file, "r") as f:
                file_read = csv.DictReader(f)
                cols = len(next(file_read))
                print(cols)
                if cols == 3:
                    all2 = []
                    for i in file_read:
                        if 0 < len(i["name"]) <= 20:
                            name = i["name"]
                            price = i["price"]
                            amount = i["quantity"]
                            all2.append(cls(name, price, amount))

                    cls.all = all2
                    return cls.all
                else:
                    raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def is_integer(value):
        if isinstance(value, int):
            return True
        if isinstance(value, float):
            return value.is_integer()
        else:
            return False

    def __repr__(self) -> str:
        return f"Item({self._name}, {self.price}, {self.amount})"

    def __str__(self) -> str:
        return f"{self._name}"


class Phone(Item):

    def __init__(self, name, price, amount, number_of_sim):
        super().__init__(name, price, amount)
        if 0 < number_of_sim:
            self._number_of_sim = number_of_sim
        else:
            raise AttributeError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if not isinstance(other, Item):
            raise AttributeError("Экземпляры класса должны быть из класса Item и/или наследуемыми от Item")
        return self.amount + other.amount

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if 0 < number_of_sim:
            self._number_of_sim = number_of_sim
        else:
            raise AttributeError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self) -> str:
        return f"Phone({self._name}, {self.price}, {self.amount}, {self._number_of_sim})"


class LanguageMixin:
    _supported_languages: tuple[str, ...] = ('RU', 'EN')

    def languages(self):
        current_language_index: int = self._supported_languages.index(self.language)
        next_language_index = (current_language_index + 1) % len(self._supported_languages)
        self.language = self._supported_languages[next_language_index]

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, value: str) -> None:
        if value not in self._supported_languages:
            raise ValueError
        self.__language = value


class KeyBoard(LanguageMixin, Item):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = "EN"
