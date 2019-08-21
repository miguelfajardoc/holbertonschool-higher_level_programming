#!/usr/bin/python3
""" find a peak """


def find_peak(list_of_integers):
    """ function that find a peak """
    if len(list_of_integers) is 0:
        return None
    index = int(len(list_of_integers) / 2)
    return (find_true_peak(list_of_integers, index))


def find_true_peak(lista, index):
    """ true function that find a peak """
    if index is not 0 and index is not len(lista):
        if lista[index] >= lista[index -
                                 1] and lista[index] >= lista[index + 1]:
            return (lista[index])
        elif lista[index - 1] >= lista[index + 1]:
            index = index - int(index / 2)
            return (find_true_peak(lista, index))
        else:
            index = index + int(index / 2)
            return (find_true_peak(lista, index))
    elif index is 0:
        if lista[index] >= lista[index + 1]:
            return (lista[index])
        else:
            index = index + int(index / 2)
            return (find_true_peak(lista, index))
    else:
        if lista[index] >= lista[index - 1]:
            return (lista[index])
        else:
            index = index - int(index / 2)
            return (find_true_peak(lista, index))
