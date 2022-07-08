import os
import unittest
from Commands_Sources.Cd import Cd
from Commands_Sources.Cp import Cp
from Commands_Sources.Ls import Ls
from Commands_Sources.Mkdir import Mkdir
from Commands_Sources.Mv import Mv
from Commands_Sources.Pwd import Pwd
from Commands_Sources.Rm import Rm
from Commands_Sources.Rmdir import Rmdir


class CommandTest(unittest.TestCase):

    def setUp(self):  # Срабатывает каждый раз при запуске тестов
        self.ls = Ls()
        self.pwd = Pwd()
        self.cd = Cd()
        self.cp = Cp()
        self.mv = Mv()
        self.rm = Rm()
        self.rmdir = Rmdir()
        self.mkdir = Mkdir()
        if not os.path.exists('testing_dir1'):  # Если директории не существует - создать
            os.system("mkdir testing_dir1")
        if not os.path.exists('testing_dir2'):
            os.system("mkdir testing_dir2")
        os.system("touch testing_dir1/testingfile1.py")  # Создаем файлы для тестов
        os.system('touch testing_dir1/testingfile2.py')

    def test_ls(self):  # Если вывод команды совпадает со списком имён настоящего пути.
        self.assertEqual(self.ls.command(), os.listdir(os.getcwd()))

    def test_pwd(self):  # Если вывод команды совпадает с настоящим путём.
        self.assertEqual(self.pwd.command(), os.getcwd())

    def test_cd(self):
        cur_path = self.cd.get_path()
        self.assertNotEqual(self.cd.command('testing_dir1'), cur_path)  # Пути должны отличаться
        self.assertEqual(self.cd.command('..'), cur_path)  # А здесь наоборот совпасть
        # Если обработчик исключений функции не сработал.
        try:
            self.cd.command('testing_dir3')
        except FileNotFoundError:
            self.fail("Raised FileNotFoundError")
        try:
            self.cd.command('testing_dir1/testingfile1.py')
        except NotADirectoryError:
            self.fail("Raised NotADirectoryError")

    def test_cp(self):
        self.cp.command('testing_dir1/testingfile1.py', 'testing_dir2/file_cd_test.py')
        self.assertTrue(os.path.exists('testing_dir2/file_cd_test.py'))  # Новый файл создался
        self.assertTrue(os.path.exists('testing_dir1/testingfile1.py'))  # Прошлый файл остался
        # Если обработчик исключений функции не сработал.
        try:
            self.cp.command('filenotfound', 'testing_dir1')
        except FileNotFoundError:
            self.fail("Raised FileNotFoundError")

    def test_mv(self):
        self.mv.command('testing_dir1/testingfile1.py', 'testing_dir2/file_mv_test.py')
        self.assertTrue(os.path.exists('testing_dir2/file_mv_test.py'))  # Новый файл создался
        self.assertFalse(os.path.exists('testing_dir1/testingfile1.py'))  # Прошлого нет
        # Если обработчик исключений функции не сработал.
        try:
            self.mv.command('filenotfound.py', 'testing_dir1')
        except FileNotFoundError:
            self.fail("Raised FileNotFoundError")

    def test_rm(self):
        self.rm.command('testing_dir2/file_mv_test.py')
        self.assertFalse(os.path.exists('testing_dir2/file_mv_test.py'))  # Файла больше нет
        # Если обработчик исключений функции не сработал.
        try:
            self.rm.command('filenotfound.py')
        except FileNotFoundError:
            self.fail("Raised FileNotFoundError")
        try:
            self.rm.command('testing_dir1')
        except IsADirectoryError:
            self.fail("Raised IsADirectoryError")

    def test_mkdir(self):
        self.mkdir.command('testing_dir3')
        self.assertTrue(os.path.exists('testing_dir3'))  # Директория создалась
        # Если обработчик исключений функции не сработал.
        try:
            self.mkdir.command('testing_dir3')
        except FileNotFoundError:
            self.fail("Raised FileNotFoundError")

    def test_rmdir(self):
        self.rmdir.command('testing_dir3')
        self.assertFalse(os.path.exists('testing_dir3'))  # Директории больше нет
        # Если обработчик исключений функции не сработал.
        try:
            self.rmdir.command('testing_dir3')
        except FileNotFoundError:
            self.fail("Raised FileNotFoundError")
        try:
            self.rmdir.command('testing_dir1/testingfile2.py')
        except NotADirectoryError:
            self.fail("Raised IsADirectoryError")


if __name__ == "__main__":
    unittest.main()
