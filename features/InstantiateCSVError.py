# -*- coding: utf-8 -*-
import csv
import os


class InstantiateCSVError(Exception):

    """
    Выбрасывает исключение, если файл csv повреждён
    Атрибуты класса:
    msg - сообщение об ошибке
    """
    def __init__(self, file):
        self.file = file
        self.msg = f"InstantiateCSVError: Файл {file} поврежден"
        super().__init__(self.msg)
