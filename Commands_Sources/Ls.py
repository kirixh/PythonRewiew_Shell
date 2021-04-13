import os

from abstract_commands import Command


class Ls(Command):
    def __init__(self):
        super().__init__()

    def command(self):
        """
        Вывод в столбик имена всех файлов и директорий для текущей директории и возвращает список имён.
        """
        self.get_path()  # обновляем текущий путь
        array = os.listdir(self.path)
        for name in array:
            print(name, end='\n')
        return array  # возвращаем список файлов
