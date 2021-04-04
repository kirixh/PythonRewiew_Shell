import os

from abstract_commands import Commands


class Mkdir(Commands):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Создать директорию с именем args[0], если ее не было.
        :param args: кортеж, args[0] - имя директории.
        """
        self.get_path()  # обновляем текущий путь
        if not os.path.isdir(args[0]):  # если такой не было
            os.mkdir(args[0])
