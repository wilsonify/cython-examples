"""
example of a compute limited function
"""
import sys


def fib(n):
    """
    calculate the nth fibonacci number
    :param n:
    :return:
    """
    a, b = 0, 1
    for i in range(n):
        a, b = a + b, a
    return a


def main(arg, numiter):
    """
    call fib many times
    :param arg:
    :param numiter:
    """
    for _ in range(numiter):
        fib(arg)


if __name__ == '__main__':
    arg_outer, numiter_outer = list(map(int, sys.argv[1:]))
    main(arg_outer, numiter_outer)
