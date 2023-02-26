from features import Item
import pytest


def test_calculate_total_price():
    assert Item.Item('Смартфон', 10000, 20).calculate_total_price() == 200000
    assert Item.Item("Ноутбук", 20000, 5).calculate_total_price() == 100000


def test_apply_discount():
    assert Item.Item(pay_rate=0.8, name="Смартфон", price=10000, amount=20).apply_discount() == 8000.0
    assert Item.Item("Ноутбук", 20000, 5).apply_discount() == 20000
