"""
someFunction
"""


def someFunction(text):
    print(f'You passed this Python program {text} from C! Congratulations!')
    return 12345


def multiply(a, b):
    print("Will compute", a, "times", b)
    c = 0
    for i in range(0, a):
        c = c + b
    return c
