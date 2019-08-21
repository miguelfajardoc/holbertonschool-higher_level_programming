#!/usr/bin/python3
""" find a peak """


def find_peak(list_of_integers):
    """ function that find a peak """
    if len(list_of_integers) is 0:
        return None
    if len(list_of_integers) is 1:
        return (list_of_integers[0])
    index = 0
    mitad = int(len(list_of_integers) / 2)
    return (find_true_peak(list_of_integers, mitad, mitad))


def find_true_peak(lista, index, mitad):
    """ true function that find a peak """
    if index is not 0 and index is not len(lista) - 1:
        if lista[index] >= lista[index -
                                 1] and lista[index] >= lista[index + 1]:
            return (lista[index])
        elif lista[index - 1] >= lista[index + 1]:
            mitad = int(mitad / 2)
            if mitad is 0:
                mitad = 1
            index = index - mitad
            return (find_true_peak(lista, index, mitad))
        else:
            mitad = int(mitad / 2)
            if mitad is 0:
                mitad = 1
            index = index + mitad
            return (find_true_peak(lista, index, mitad))
    elif index is 0:
        if lista[index] >= lista[index + 1]:
            return (lista[index])
        else:
            mitad = int(mitad / 2)
            if mitad is 0:
                mitad = 1
            index = index + mitad
            return (find_true_peak(lista, index, mitad))
    else:
        if lista[index] >= lista[index - 1]:
            return (lista[index])
        else:
            mitad = int(mitad / 2)
            if mitad is 0:
                mitad = 1
            index = index - mitad
            return (find_true_peak(lista, index, mitad))
