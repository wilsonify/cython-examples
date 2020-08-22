"""
someFunction
"""


def some_function(text: str) -> int:
    """
    string in a string
    :param text:
    :return:
    """
    print(f'You passed this Python program {text} from C! Congratulations!')
    return 12345


def multiply(multiplier: float, multiplicand: float) -> float:
    """
    multiplication
    :param multiplier:
    :param multiplicand:
    :return:
    """
    print("Will compute", multiplier, "times", multiplicand)
    result = 0
    for _ in range(0, multiplier):
        result = result + multiplicand
    return result


def main():
    """
    entrypoint
    :return:
    """
    print(f"2 * 3 = {multiply(2, 3)}")


if __name__ == "__main__":
    main()
