# PythonKnightsSG

## Overview of Study Group

We’ll be using Mark Pilgrim’s Dive Into Python3 for our study material.  We may also use the following as supporting material.

* http://www.diveintopython.net/toc/index.html
* http://www.diveintopython3.net/
* http://learnpythonthehardway.org/
* http://learnpythonthehardway.org/book/
* https://docs.python.org/2/tutorial/index.html
* https://docs.python.org/3.5/tutorial/index.html

Games with Python:  http://codecombat.com/

## Development Environment

* [Sublime Text 3](http://www.sublimetext.com/3)
* Plug-ins
  * [Anaconda](https://packagecontrol.io/packages/Anaconda)
  * [Python Improved](https://packagecontrol.io/packages/Python%20Improved)
* Project Configurations

```
{
  "build_systems":
  [
    {
      "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
      "name": "Anaconda Python Builder",
      "selector": "source.python",
      "shell_cmd": "/opt/boxen/homebrew/Cellar/python3/3.4.3/bin/python3 -u \"$file\""
    }
  ],
  "folders":
  [
    {
      "path": "~/repos/PythonKnightsSG"
    }
  ],
  "settings":
  {
    "anaconda_gutter_marks": true,
    "anaconda_gutter_theme": "alpha",
    "anaconda_linter_mark_style": "outline",
    "anaconda_linting": true,
    "anaconda_linting_behaviour": "always",
    "enable_signatures_tooltip": true,
    "extra_paths":
    [
      "~/repos/PythonKnightsSG/week01"
    ],
    "merge_signatures_and_doc": true,
    "pep257": true,
    "python_interpreter": "/opt/boxen/homebrew/Cellar/python3/3.4.3/bin/python3",
    "test_command": "python3 -m unittest discover \"$file\"",
    "use_pylint": false,
    "validate_imports": true
  }
}
```