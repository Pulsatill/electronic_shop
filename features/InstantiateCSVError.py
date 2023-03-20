# -*- coding: utf-8 -*-
import csv
import os


class InstantiateCSVError(Exception):

    """
    Выбрасывает исключение, если файл items.csv повреждён
    Атрибуты класса:
    msg - сообщение об ошибке
    """
    def __init__(self):
        self.msg = "InstantiateCSVError: Файл item.csv поврежден"
        super().__init__(self.msg)
