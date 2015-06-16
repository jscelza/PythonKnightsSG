# Week 4
## Homework

* Read Chapter 4 & 5
  * http://www.diveintopython3.net/strings.html
  * http://www.diveintopython3.net/regular-expressions.html

## Notes from Readings - Chapter 4

* 4.3 Diving in
  * no such thing as string encoded
  * Bytes are not characters; bytes are bytes. Characters are an abstraction. A string is a sequence of those abstractions
* 4.4 Formating Strings
  * Support formatting values into strings
  * example: '{0}'s password is {1}".format(username, password)'
  * Compound field Names: format specifiers can access items and properties of data structures using (almost) Python syntax.
  * The following compandfield names "just work"
    * Passing a list, and accessing an item of the list by index
    * Passing a dictionary, and accessing a value of the dictionary by key
    * Passing a module, and accessing its variables and functions by names
    * Passing a class instance, and accessing its properties and methods by name
    * Any combination of the above
  *  Format Specifiers
    * further refines how the replaced variable should be formatted.
    * allow you to munge the replacement text in a variety of ways.
* 4.6 Strings vs Bytes
  * Bytes are bytes; characters are an abstraction.
  * An immutable sequence of Unicode characters is called a string.
  * An immutable sequence of numbers-between-0-and-255 is called a bytes object.
  * NEVER an mix bytes and strings

*

## Further Readings


## Learn Python the Hardway

* Readings
* Location for this weeks exercise

## Helpful things found in reading

* Python 3 assumes that your source code — i.e. each .py file — is encoded in utf-8.
* to change encoding add the below to the file line (2nd if you have a #!) of your file
```
# -*- coding: windows-1252 -*-
```
