## PythonReview Shell

### **Possible commands:**

`ls` - Output a list of files and directories for the current directory and return the list.

`pwd` - Print the full path for the current directory and return path.

`cd [path]` - Change current directory by a relative or absolute path and return new path.

`cp [filename1] [filename2]` - Copy [filename1] into [filename2]. Files with the same name are overwritten.

`mv [filename1] [filename2]` - Move the [filename1] to [filename2].
If the directories match, they are renamed.
Files with the same name are overwritten.
If the path to the directory is specified as [filename2], the name of the moved file will not change.

`rm [filename]` - Delete the file.

`rmdir [dirname]` - Delete the directory if it's empty.

`mkdir [dirname]` - Make directory if it didn't exist.

`exit` - Stop the program.

## Examples of using the program

![img.png](screenshots/img.png)
![img.png](screenshots/img1.png)
![img_1.png](screenshots/img_1.png)
![img_2.png](screenshots/img_2.png)
![img_3.png](screenshots/img_3.png)
![img_4.png](screenshots/img_4.png)

## How to install and run in PyCharm

1) Open or create a project
2) run in Terminal: `git clone https://github.com/kirixh/PythonRewiew_Shell.git -b dev`
3) Open main.py -> click RMB -> Run 'main'

### **Project has unittest system:**
To run tests: Open tests.py -> click RMB -> Run 'tests'