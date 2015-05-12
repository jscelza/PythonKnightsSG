# Week 3
## Homework

* Read Chapter 3
  * http://www.diveintopython3.net/comprehensions.html

## Notes from Readings - Chapter 3

* 3.2 Working with files and directories
  * See Function secion below around modules
* 3.3 List Comprehensions
*

## Further Readings

* https://docs.python.org/3.1/library/os.html
*

## Learn Python the Hardway

* Readings
* Location for this weeks exercise

## Helpful Function found in reading

* `import os.path` module
  * `os.path.join("dir","filename")` -->  constructs a pathname out of one or more partial pathnames
  * `os.path.expanduser('~')` --> expands directory variable
  * `os.path.split('pathname')` --> creates a tulple of filename and directory
  * `os.path.splitext('filename')` --> creates a tuple of shortname and extension.
  * `os.path.realpath('filename')` --> using the obsolute path and filename
* `import os` module
  * `os.getcwd()` --> get current working directory
  * `os.chdir('/directory')` --> Change directory
  * `os.stat('filename')` --> returns an object that contains several different types of metadata about the file
* `import glob` module
  * `glob.glob('filename regex')`  --> list of files matching the regex
* `time.localtime(time)` --> converts from Epoch to structure format.