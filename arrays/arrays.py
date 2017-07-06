import random

def even_odd(A):
    """given an array of integers, move all evens to the front. in place"""
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A

def dutch_flag_partition(pivot_index, A):
    """partition array so that everything less than pivot_index is
    smaller than the pivot"""
    pivot = A[pivot_index]
    # first pass - group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    # second pass - group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

    return A

def plus_one(A):
    """given an array representing digits of an int, add one to the int"""
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] < 10:
            break
        elif A[i] == 10:
            A[i] = 0
            A[i - 1] += 1

    if A[0] == 10:
        A[0] = 0
        A.insert(0, 1)

    return A

def buy_sell_stock_once(prices):
    """given an array representing stock prices, find max profit"""
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)

    return max_profit

def random_subset(A, k):
    """given an array, and int k, generate a random subset of arr of length k,
    return it in the the arr, s.t. arr[:k] is the subset."""
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

    return A
