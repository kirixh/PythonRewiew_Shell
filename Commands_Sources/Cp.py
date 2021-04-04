import os

from abstract_commands import Commands
from shutil import copy


class Cp(Commands):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Копирование файла по адресу args[0] в файл(директорию) по адресу args[1].
        Файлы с одинаковым именем перезаписываются.
        :param args: кортеж, args[0] - что копируем, args[1] - куда.
        """
        self.get_path()  # обновляем текущий путь
        # делаем из относительных путей абсолютные и копируем
        copy(os.path.abspath(args[0]), os.path.abspath(args[1]))
