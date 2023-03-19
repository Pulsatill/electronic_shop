import pytest
from features.Item import KeyBoard

kb1 = KeyBoard('Dark Project KD87A', 9600, 5)
kb2 = KeyBoard("Logitech V800 12000", 5000, 12)


def test_change_lang():
    assert kb1.language == "EN"
    kb1.change_lang()
    assert kb1.language == "RU"
    assert kb2.language == "EN"
    kb1.change_lang()
    assert kb1.language == "EN"


def test_str():
    assert kb1.__str__() == "Dark Project KD87A, 9600, 5"
    assert kb2.__str__() == "Logitech V800 12000, 5000, 12"
