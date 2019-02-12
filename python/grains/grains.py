
def on_square(integer_number: int) -> int:
    if integer_number < 1 or integer_number > 64:
        raise ValueError("Input number is negative, zero, or over 64")
    return 2 ** (integer_number-1)


def total_after(integer_number: int) -> int:
    if integer_number < 1 or integer_number > 64:
        raise ValueError("Input number is negative or zero, or over 64")

    return sum([2 ** i for i in range(integer_number)])
