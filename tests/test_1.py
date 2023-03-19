import pytest
import os
from features.Item import Item

item1 = Item('Смартфон', 10000, 20, pay_rate=0.8)
item2 = Item("Ноутбук", 20000, 5)
pay_rate = 0.8


@pytest.fixture
def csv_file():
    csv_file = os.path.join("test.csv")
    return csv_file


def test_str():
    assert item1.__str__() == "Смартфон"
    assert item2.__str__() == "Ноутбук"


def test_repr():
    assert item1.__repr__() == "Item(Смартфон, 10000, 20)"
    assert item2.__repr__() == "Item(Ноутбук, 20000, 5)"


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    assert item1.apply_discount() == 8000.0
    assert item2.apply_discount() == 20000


def test_name():
    with pytest.raises(AttributeError):
        Item("Квадрокоптер 15000 V800", 25000, 1)
    with pytest.raises(AttributeError):
        item2.name = "Квадрокоптер 15000 V800"
    assert item2.name == "Ноутбук"


def test_instantiate_from_csv(csv_file):
    Item.instantiate_from_csv(csv_file)
    item4 = Item.all[0]
    item5 = Item.all[1]
    item6 = Item.all[2]

    assert len(Item.all) == 4
    assert item4.name == "Ноутбук"
    assert item5.price == "10"
    assert item6.amount == "5"
    item4.price = 5.6
    item5.price = 1000
    item6.amount = 6.1
    assert Item.is_integer(item4.price) == False
    assert Item.is_integer(item5.price) == True
    assert Item.is_integer(item6.amount) == False


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.5) == False
