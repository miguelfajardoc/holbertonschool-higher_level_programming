#!/usr/bin/python3
""" find a peak """


def find_peak(list_of_integers):
    """ function that find a peak """
    if len(list_of_integers) is 0:
        return None
    index = 0
    mitad = int(len(list_of_integers) / 2)
    return (find_true_peak(list_of_integers, index, mitad))


def find_true_peak(lista, index, mitad):
    """ true function that find a peak """
    if index is not 0 and index is not len(lista) - 1:
        if lista[index] >= lista[index -
                                 1] and lista[index] >= lista[index + 1]:
            return (lista[index])
        elif lista[index - 1] >= lista[index + 1]:
            index = index - mitad
            mitad = int(mitad / 2)
            return (find_true_peak(lista, index, mitad))
        else:
            index = index + mitad
            mitad = int(mitad / 2)
            return (find_true_peak(lista, index, mitad))
    elif index is 0:
        if lista[index] >= lista[index + 1]:
            return (lista[index])
        else:
            index = index + mitad
            mitad = int(mitad / 2)
            return (find_true_peak(lista, index, mitad))
    else:
        if lista[index] >= lista[index - 1]:
            return (lista[index])
        else:
            index = index - mitad
            mitad = int(mitad / 2)
            return (find_true_peak(lista, index, mitad))
