#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {}".format(a, op, b, result))
