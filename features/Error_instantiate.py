"""
Пытался интегрировать статик метод is_integer таким образом
Но сразу выдаёт ошибку, не понимаю как вылечить
Вроде бы через i[value] он должен получать value, т.е. целое число, но выдаёт ошибку
Что делать?
"""


def instantiate_from_csv(cls):
    with open("items.csv", newline="") as f:
        all2 = []
        file_read = csv.DictReader(f)
        for i in file_read:
            name = i["name"]
            if cls.is_integer(i["price"]) is True:
                price = i["price"]
            else:
                price = i["price"]
                print("Проверьте правильность выставления цены")
            if cls.is_integer(i["quantity"]) is True:
                amount = i["quantity"]
            else:
                raise ValueError("Неверное количество!")
            all2.append(cls(name, price, amount))
        cls.all = all2
        return cls.all
