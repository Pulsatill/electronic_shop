import pytest
from features.Item import Phone

phone1 = Phone("iPhone 14", 120000, 5, 1)
phone2 = Phone("Xiaomi 13", 40000, 23, 2)


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
