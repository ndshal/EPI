import string
from functools import reduce
import math

def int_to_string(x):
    """Convert int to string"""
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while x > 0:
        s.append(chr(ord('0') + x % 10))
        x //= 10

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    """Convert string to int"""
    return reduce(
        lambda running_sum, c: running_sum*10 + string.digits.index(c),
        s[s[0] == '-':], 0
        )*(-1 if s[0] == '-' else 1)

def convert_decimal_to_base(s, b):
    num = int(s)
    power = int(math.log(num, b))
    digits = []

    while num > 0:
        digit = num // b**power
        digits.append(str(digit))
        num -= digit * b**power
        power -= 1

    return ''.join(reversed(digits))

def convert_base(s, b1, b2):
    """Convert string representation of an integer from b1 to b2"""
    def convert_decimal_to_base(s, b):
        num = int(s)
        power = int(math.log(num, b))
        digits = []

        while power >= 0:
            digit = num // b**power
            digits.append(str(digit))
            num -= digit * b**power
            power -= 1

        return ''.join(reversed(digits))

    def convert_base_to_decimal(s, b):
        dec = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
        }

        return str(reduce(lambda acc, el: acc + el, (dec[s[~i]] * b**i for i in range(len(s)))))

    return convert_decimal_to_base(convert_base_to_decimal(s, b1), b2)
