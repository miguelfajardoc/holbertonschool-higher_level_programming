#!/usr/bin/python3
from sys import argv


def check_sol(list_s, queen, n):
    """check if the queen position is validate to the list_s"""
    cnt = 0
    if len(list_s) == 0:
        return(True)
    while cnt < len(list_s):
        f, c = list_s[cnt][0], list_s[cnt][1]
        if f == queen[0] or c == queen[1]:
            return(False)
        else:
            p_ddc = c
            p_df = f
            p_ic = c
            while p_df < queen[0]:
                p_ddc += 1
                p_df += 1
                p_ic -= 1
                if p_ddc < n and p_df == queen[0] and p_ddc == queen[1]:
                    return(False)
                elif p_ic >= 0 and p_df == queen[0] and p_ic == queen[1]:
                    return(False)
        cnt += 1
    return(True)


def generator(list_s, test_b, result, n):
    """generate the next queen position to set according to:
    if the previus queen fail, send next column position, if
       no more position exist, send 0.
    if the previus queen pass, send next row position with 0 column.
       if no more position exist, send backtrace signal (-1)
    """
    if len(list_s) == 0 and result is True:
        return (test_b)
    if result is True:
        if test_b[0] + 1 == n:
            return(0)
        test_b[0] += 1
        test_b[1] = 0
        return (test_b)
    else:
        if test_b[1] + 1 == n:
            if len(list_s) == 0:
                return ("exit")
            return (-1)
        test_b[1] += 1
        return (test_b)


list_s = []
s = 0
n = 0
status = True
solutions = []
queen = [0, 0]
if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    n = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
while len(list_s) < n+1:
    queen = generator(list_s, queen, status, n)
    if queen == "exit":
        exit()
    if queen == 0:
        if len(solutions) != 0:
            for i in solutions:
                if i == list_s:
                    queen = -1
                    break
        print(list_s)
        if queen != -1:
            solutions.append(list_s)
            list_s = list_s[:]
            queen = -1
    if queen == -1:
        queen = list_s.pop()
        status = False
    else:
        if check_sol(list_s, queen, n):
            list_s += [queen[:]]
            status = True
        else:
            status = False
