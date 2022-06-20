#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx = 0
    newlist = []
    for idx in range(list_length):
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            continue
        except (ZeroDivisionError, ValueError):
            print("divison by 0")
            continue
        except IndexError:
            print("out of range")
        finally:
            newlist.append(result)
    return newlist
