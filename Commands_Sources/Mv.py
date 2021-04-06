import os

from abstract_commands import Command


class Mv(Command):
    def __init__(self):
        super().__init__()

    def command(self, *args):
        """
        Перемещение файла args[0] по адресу args[1].
        Если директории совпадают - происходит переименовывание.
        Файлы с одинаковым именем перезаписываются.
        Если в качестве args[1] указан путь до директории, то имя перемещенного файла не изменится.
        :param args: кортеж, args[0] - что перемещаем, args[1] - куда.
        """
        self.get_path()  # обновляем текущий путь
        try:
            if os.path.isdir(args[1]):  # если args[1] - путь до директории
                # дописываем к пути имя исходного файла
                os.replace(args[0], os.path.join(args[1], os.path.split(args[0])[1]))
            else:
                os.replace(args[0], args[1])
        except IsADirectoryError:
            print("You are trying to move directory!")
        except FileNotFoundError:
            print("File does not exist")
