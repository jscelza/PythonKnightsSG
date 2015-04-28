# Week 1
## Homework

* Get a Github account
* Read Chapter -1, 0, 1
  * http://www.diveintopython3.net/whats-new.html
  * http://www.diveintopython3.net/installing-python.html
  * http://www.diveintopython3.net/your-first-python-program.html

## Notes from Readings

* Chapter 1
  * 1.3.1 docstrings
    * Needs to be on the line following any function def
    * """  multiple line documentationa """
    * One-liners are for really obvious cases. They should really fit on one line
    * Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description
  * 1.4.1 Search path
    * see [funWithSys script](./funWithSys.py)
  * 1.5 Objects
    * Everything in Python is an object, and everything can have attributes and methods
    * In Python, the definition is looser. Some objects have neither attributes nor methods, but they could. Not all objects are subclassable. But everything is an object in the sense that it can be assigned to a variable or passed as an argument to a function.
  * 1.6 Indenting
    * Python functions have no explicit begin or end, and no curly braces to mark where the function code starts and stops.
    * The only delimiter is a colon (:) and the indentation of the code itself.
    * Code blocks are defined by their indentation.
  * 1.7 Exceptions
    * Python encourages the use of exceptions, which you handle.
    * When an error occurs in the Python Shell, it prints out some details about the exception and how it happened, and that’s that. This is called an unhandled exception.
    * If you know a line of code may raise an exception, you should handle the exception using a try...except block.
    * The syntax for raising an exception is simple enough. Use the raise statement, followed by the exception name, and an optional human-readable string for debugging purposes.
  * 1.7.1 Catching import errors
    * One of Python’s built-in exceptions is ImportError, which is raised when you try to import a module and fail.
    * Another common use of the ImportError exception is when two modules implement a common api, but one is more desirable than the other.
  * 1.8 Unbound Variables
    * You never declare the variable multiple, you just assign a value to it. That’s OK, because Python lets you do that.
    * Python will not let you do is reference a variable that has never been assigned a value
* Further Readings
  * [docstring conventions](https://www.python.org/dev/peps/pep-0257/)
  * [Documentation Strings](https://docs.python.org/3.1/tutorial/controlflow.html#documentation-strings)
  * [Style Guide for Pythong](https://www.python.org/dev/peps/pep-0008/)
  * [Tutorial](http://docs.python.org/tutorial/)
  * [Porting 2 code to 3](http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html)
  * [Package Manager](https://pypi.python.org/pypi)
  * [Special Method Names](http://www.diveintopython3.net/special-method-names.html)

## Learn Python the Hardway

* [Exercise 1](http://learnpythonthehardway.org/book/ex1.html)
* [Exercise 2](http://learnpythonthehardway.org/book/ex2.html)
* [Exercise 3](http://learnpythonthehardway.org/book/ex3.html)
* [Exercise 4](http://learnpythonthehardway.org/book/ex4.html)
* [Exercise 5](http://learnpythonthehardway.org/book/ex5.html)
* [Exercise 6](http://learnpythonthehardway.org/book/ex6.html)
* [Exercise 7](http://learnpythonthehardway.org/book/ex7.html)
* [Exercise 8](http://learnpythonthehardway.org/book/ex8.html)
* [Exercise 9](http://learnpythonthehardway.org/book/ex8.html)
* [Exercise 10](http://learnpythonthehardway.org/book/ex8.html)

## Helpful Function found in reading

* type()
  * *Example*: type(x) is int
  * *Returns*: True or False
* isinstance()
  * *Example*: isinstance(x, int)
  * *Returns*: True or False