import os

from abstract_commands import Command


class Rmdir(Command):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Удаление директории по адресу args[0], если она пуста.
        :param args: кортеж, args[0] - путь к директории.
        """
        self.get_path()  # обновляем текущий путь
        try:
            os.rmdir(args[0])
        except NotADirectoryError:
            print("It's not a directory!")
        except FileNotFoundError:
            print("Directory not found!")
