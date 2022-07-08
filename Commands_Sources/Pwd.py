from abstract_commands import Command


class Pwd(Command):
    def __init__(self):
        super().__init__()

    def command(self):
        """
        Вывод полного пути к текущей директории и возврат пути.
        """
        self.get_path()  # обновляем текущий путь
        print(self.path)
        return self.path  # возвращаем текущий путь
