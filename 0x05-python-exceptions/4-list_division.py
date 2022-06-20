#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for idx in range(list_length):
        result = 0
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except (ZeroDivisionError, ValueError):
            print("divison by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            newlist.append(result)
    return newlist
