#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0:
        return copy
    elif idx > len(copy) - 1:
        return copy
    else:
        copy.remove(my_list[idx])
        copy.insert(idx, element)
        return copy
