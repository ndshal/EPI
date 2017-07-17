import string
import functools
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
    return functools.reduce(
        lambda running_sum, c: running_sum*10 + string.digits.index(c),
        s[s[0] == '-':], 0
        )*(-1 if s[0] == '-' else 1)

def convert_base(num_as_string, b1, b2):
    """Convert string representation of an integer from b1 to b2"""
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))

def replace_and_remove(size, s):
    """Given an array of chars, delete every 'b' and replace every 'a'
    with two 'd's"""
    # if we insert and delete using built-in methods, thats O(n^2) time
    # if we build an entirely new array, thats O(n) space.

    # insight: if there are no a's, iterate through and move over all chars
    # if there are no b's, ...

    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1

    return s

def is_palindrome(s):
    return False
