#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = 0
    weighted_sum = 0
    new_list = my_list.copy()

    if len(new_list) == 0:
        return 0
    else:
        for item in new_list:
            weight, value = item[1], item[0]
            total_weight += weight
            weighted_sum += weight * value

        result = weighted_sum / total_weight

    return result
