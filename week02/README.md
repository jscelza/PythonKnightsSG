# Week 2
## Homework

* Read Chapter 2
  * http://www.diveintopython3.net/native-datatypes.html

## Notes from Readings - Chapter 2

* 2.1 Important Datatypes
  * *Booleans*: True or False
  * *Numbers*: Integers, floats, fractions, or complex numbers
  * *Strings*: sequences of Unicode characters
  * *Bytes and byte arrays*: e.g. JPEG image file
  * *Lists*: ordered sequences of values
  * *Tuples*: ordered, immutable sequences of values
  * *Sets*: unordered bags of values
  * *Dictionaries*: unordered bags of key-value pairs
* 2.3.1 Coercing Integers to Floats and Vice-versa
  * some operators(like addition) will coerce integers to float point number as needed
  * To manually coerce use *float*() or *int*()
* 2.3.2 Common Numberical Operations
  * */* --> Float point division
  * *//* --> integer division
    * when positive it "truncates" to - decimal places
    * when negative it rounds "up" to the nearest integer
    * if numerator or denominator or float so will the return value but still rounded
  * ** --> "raised to the power of"
  * *%* --> gives the remainder after performing integer devision
* 2.4.3 Adding items to A Lists
  * *a_list = a_list + ['itemA', 'itemB']*  --> Create new list of the current `a_list` including items between `[]`
  * *a_list.append('item')* --> Append a single `'item'` to the end of the list
  * *a_list.insert(pos, 'item')* --> insert  `'item'` in position `pos`
* 2.4.4 Searching for values in a list
  * *a_list.count('item')* --> Count number of `item` in `a_list`
  * *a_list.index('item')* --> Finds the poistions of `'item'`
  * *'item' in a_list* --> Conditional (T/F) to check if `'item'` exists in `a_list`
* 2.4.5 Removing Items from a List
  * *del a_list[pos]*  --> Remove an item from a specific `pos` in `a_list`
  * *a_list.remove('my item')* --> Removes the item that match the value of `'my item'`
  * *a_list() or a_list(pos)* --> Removes the last item in the list or if a `pos` is passed then item in that position
* 2.4.7 Tuples
  * Immutable lists (no add or remove)
  * Faster then lists.
  * Best for constant set of values that you iterate trough
  * Some Tuples can be use as dictionary keys (like final static in java?)



## Further Readings


## Learn Python the Hardway

* Readings
* Location for this weeks exercise

## Helpful Function found in reading

