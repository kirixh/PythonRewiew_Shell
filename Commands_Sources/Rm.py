import os

from abstract_commands import Commands


class Rm(Commands):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Удаление файла с именем args[0], если такой существует.
        :param args: кортеж, args[0] - имя удаляемого файла.
        """
        self.get_path()  # обновляем текущий путь
        os.remove(args[0])
