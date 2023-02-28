import pytest
from features.Item import Item

item1 = Item('Смартфон', 10000, 20, pay_rate=0.8)
item2 = Item("Ноутбук", 20000, 5)
pay_rate = 0.8


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    assert item1.apply_discount() == 8000.0
    assert item2.apply_discount() == 20000
