#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    string = dir(hidden_4)
    l = len(string)
    for i in range(l):
        if string[i][0] != '_':
            print(string[i])
