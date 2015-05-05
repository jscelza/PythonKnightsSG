"""Run some basic fraction functions.

http://www.diveintopython3.net/native-datatypes.html

Need to understand why command line out puts Fractions(x, y)
and print gives the value

Available Functions

display_fraction_info(int, int)
  Function to print out what a num. and dom is.

display_pi_info(int, string)
  function to print out some fun with PI

is_it_true(string)
  function to determine if datatype is true/false

output_list(list)
  function to print out values of a list in multiple ways
"""

import fractions
import math


def display_fraction_info(numerator, denominator=1):
    """Function to display info about a fraction."""
    if denominator == 0:
        print('Denominator can not equal 0. Exiting.')
        exit()

    print("Top =", numerator)
    print("Bottom =", denominator)

    return fractions.Fraction(numerator, denominator)


def display_pi_info(my_number, trig_action="sin"):
    """Function to display info around PI calulation."""
    print("PI equals", math.pi)
    print("My Number is", my_number)
    print("Trigonometric function:", trig_action)
    print("Value of", trig_action, "after dividing PI by", my_number, end=' ')
    print("is", getattr(math, trig_action)(math.pi / my_number))
    print()


def is_it_true(anything):
    """checking for Numbers in a boolean context."""
    print("Is the context of %s true or false?" % anything, end=' ')
    if anything:
        print("yes, it true")
    else:
        print("no, it's false")


def output_list(my_list):
    """Loop thru a list and output it."""
    print("The Values of my_list is")
    for s in my_list:
        print(s)

    print(my_list[1:-1])
    print(my_list[3:])
    print(my_list[:3])
    print(my_list[:])
    print("The length of my_list is", len(my_list))


if __name__ == '__main__':

    print("Some code to play with Integers, Fraction and Math")
    a_num = display_fraction_info(1, 3)
    print("a_num equals", a_num)
    time_by = 2
    print("Multiple by", time_by, "equals", end=' ')
    print(a_num * time_by)
    print()

    print("Some code to play with Math, PI and Geomtry")
    display_pi_info(2, "sin")
    display_pi_info(4, "tan")
    print()

    print("Some code to play with Booleans Lists")
    is_it_true(1)
    is_it_true(-1)
    is_it_true(0)
    is_it_true(0.0)
    print()

    print("Some code to play with Lists")
    a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
    output_list(a_list)
    print()
    print("Adding elements")
    a_list = a_list + [2.0, 3]
    output_list(a_list)
    print()
    a_list.append(True)
    output_list(a_list)
    print()
    a_list.insert(0, 'Ω')
    output_list(a_list)
    print()
    a_list.extend(['four', '99'])
    output_list(a_list)
    print()
    print("Removing elements")
    a_list.remove('four')
    output_list(a_list)
    print()
    del a_list[1]
    output_list(a_list)

    print("Some code to play with tuples")
    a_tuple = ("a", "b", "mpilgrim", "z", "example")
    print(a_tuple)
    print("'example' lives in position", a_tuple.index("example"))
    print("Is 'z' in my tuple?", "z"in a_tuple)
    # a_tuple.remove('z')
    output_list(a_tuple)
