import os

from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self):
        """
        self.path: поле, в котором содержится путь до текущей директории
        """
        self.path = os.getcwd()

    def get_path(self):
        """
        Обновляет параметр path, так как он
        мог измениться во время выполнения других команд.
        """
        self.path = os.getcwd()

    @abstractmethod
    def command(self, *args):
        pass
