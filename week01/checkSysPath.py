'''Playing with sys by using examples from Chapter 1

    http://www.diveintopython3.net/your-first-python-program.html

'''

import sys

print("sys.path has the following value:")
print(sys.path)

print()
print("sys has the following value: ")
print(sys)

pythonKnightPath = "~/repos/PythonKnightsSG"
print()
print("Adding PythonKnightsSG repo to path")
sys.path.insert(0, pythonKnightPath)
print(sys.path)
