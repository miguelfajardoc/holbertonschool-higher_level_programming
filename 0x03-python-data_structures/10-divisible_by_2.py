#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_list = []
    for i in my_list:
        if i % 2 == 0:
            true_list.append(True)
        else:
            true_list.append(False)
    return(true_list)
