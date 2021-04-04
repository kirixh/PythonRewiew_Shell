import os

from abstract_commands import Commands


class Cd(Commands):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Меняет текущую директорию на args[0]
        :param args: кортеж, args[0] - новый адрес.
        """
        os.chdir(args[0])
        self.get_path()  # обновляем текущий путь
