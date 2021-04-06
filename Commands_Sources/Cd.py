import os

from abstract_commands import Command


class Cd(Command):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Меняет текущую директорию на args[0]
        :param args: кортеж, args[0] - новый адрес.
        """
        try:
            os.chdir(args[0])
        except FileNotFoundError:
            print("Wrong path!")
        except NotADirectoryError:
            print("It's not a directory!")
        self.get_path()  # обновляем текущий путь
