import os

from abstract_commands import Commands


class Rmdir(Commands):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Удаление директории по адресу args[0], если она пуста.
        :param args: кортеж, args[0] - путь к директории.
        """
        self.get_path()  # обновляем текущий путь
        os.rmdir(args[0])
