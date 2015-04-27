"""Playing with sys by using examples from Chapter 1.

http://www.diveintopython3.net/your-first-python-program.html

Available Functions"
printSyspath()
  Print value of sys.path

addDirToSyspath(string)
  Adds string to sys.path

"""

import sys


def diplay_syspath():
    """Print sys.path value."""
    print("sys.path has the following value:")
    print(sys.path)
    print()


def add_dir_to_Syspath(pythonKnightPath='./'):
    """Add a directory to sys.path."""
    print("Adding", pythonKnightPath, " to path")
    print()
    sys.path.insert(0, pythonKnightPath)


if __name__ == '__main__':
    print('Default Value')
    diplay_syspath()

    add_dir_to_Syspath("~/repos/PythonKnightsSG")
    print('Value after inserting of directory')
    diplay_syspath()

    add_dir_to_Syspath()
    print('Value after inserting of directory')
    diplay_syspath()
