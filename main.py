from Commands_Sources.Cd import Cd
from Commands_Sources.Cp import Cp
from Commands_Sources.Ls import Ls
from Commands_Sources.Mkdir import Mkdir
from Commands_Sources.Mv import Mv
from Commands_Sources.Pwd import Pwd
from Commands_Sources.Rm import Rm
from Commands_Sources.Rmdir import Rmdir

print("Hello! This is shell on python. Possible commands:\n"
      "ls - Output a list of files and directories for the current directory.\n"
      "pwd - Print the full path for the current directory.\n"
      "cd <path> - Change current directory by a relative or absolute path.\n"
      "cp <filename1> <filename2> - Copy filename1 into filename2.\n"
      "mv <filename1> <filename2> - Move the filename1 to filename2.\n"
      "rm <filename> - Delete the file.\n"
      "rmdir <dirname> - Delete the directory if it's empty.\n"
      "mkdir <dirname> - Make directory if it didn't exist.\n"
      "exit - Stop the program.\n")
ls = Ls()
pwd = Pwd()
cd = Cd()
cp = Cp()
mv = Mv()
rm = Rm()
rmdir = Rmdir()
mkdir = Mkdir()
commands = {'ls': ls, 'pwd': pwd, 'cd': cd, 'cp': cp,
            'mv': mv, 'rm': rm, 'rmdir': rmdir, 'mkdir': mkdir}
while True:
    cm = input().split()
    if cm[0] == 'exit':
        break
    try:
        commands[cm[0]].command(*cm[1:])
    except Exception as exc:
        print(exc)
