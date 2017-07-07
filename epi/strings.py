import string
from functools import reduce

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
