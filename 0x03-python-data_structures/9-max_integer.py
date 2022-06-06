#!/usr/bin/python3
def max_integer(my_list=[]):
    _max = 0
    for item in my_list:
        if item > _max:
            _max = item
    return _max
