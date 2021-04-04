import os

from abstract_commands import Commands


class Ls(Commands):
    def __init__(self):
        super().__init__()

    def command(self):
        """
        Вывод в столбик имена всех файлов и директорий для текущей директории.
        """
        self.get_path()  # обновляем текущий путь
        for name in os.listdir(self.path):
            print(name, end='\n')
