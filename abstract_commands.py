import os

from abc import ABC, abstractmethod


class Commands(ABC):
    def __init__(self):
        self.path = os.getcwd()

    @abstractmethod
    def command(self, *args):
        pass


cm1 = Commands()
print(cm1.path)
