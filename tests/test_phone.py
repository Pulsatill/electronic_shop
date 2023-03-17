import pytest
from features.Item import Phone, Item

phone1 = Phone("iPhone 14", 120000, 5, 1)
phone2 = Phone("Xiaomi 13", 40000, 23, 2)
item1 = Item("Samsung 7", 10000, 20)


class Notebook:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


def test_init():
    with pytest.raises(AttributeError):
        Phone("Moto RV3", 15000, 1, -1)


def test_number_of_sim():
    assert phone1.number_of_sim == 1
    assert phone2.number_of_sim == 2
    with pytest.raises(AttributeError):
        phone1.number_of_sim = 0


def test_repr():
    assert phone1.__repr__() == "Phone(iPhone 14, 120000, 5, 1)"
    assert phone2.__repr__() == "Phone(Xiaomi 13, 40000, 23, 2)"


def test_add():
    assert phone1.__add__(phone2) == 28
    assert phone2.__add__(item1) == 43
    with pytest.raises(AttributeError):
        assert phone1.__add__(Notebook("Moto RV3", 15000, 1, 2))
