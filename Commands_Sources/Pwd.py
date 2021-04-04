from abstract_commands import Commands


class Pwd(Commands):
    def __init__(self):
        super().__init__()

    def command(self):
        """
        Вывод полного пути к текущей директории.
        """
        self.get_path()  # обновляем текущий путь
        print(self.path)
