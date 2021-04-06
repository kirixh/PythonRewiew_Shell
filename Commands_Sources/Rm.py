import os

from abstract_commands import Command


class Rm(Command):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Удаление файла с именем args[0], если такой существует.
        :param args: кортеж, args[0] - имя удаляемого файла.
        """
        self.get_path()  # обновляем текущий путь
        try:
            os.remove(args[0])
        except FileNotFoundError:
            print("File not found!")
