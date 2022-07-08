import os

from abstract_commands import Command


class Mkdir(Command):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Создать директорию с именем args[0], если ее не было.
        :param args: кортеж, args[0] - имя директории.
        """
        self.get_path()  # обновляем текущий путь
        try:
            os.mkdir(args[0])
        except FileExistsError:
            print("Directory already exists!")
