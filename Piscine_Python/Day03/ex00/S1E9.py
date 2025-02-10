from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, first_name, last_name, status):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status


class Stark(Character):
    """Your docstring for Class"""
    #your code here
    def __init__(self, first_name=None, last_name=None, status=None):
        super().__init__(first_name, last_name, status)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
