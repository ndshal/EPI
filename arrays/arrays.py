# given an array of integers, move all evens to the front. in place
def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A

# partition array so that everything less than pivot_index is
# smaller than the pivot
def dutch_flag_partition(pivot_index, A):
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

# given an array representing digits of an int, add one to the int
def plus_one(A):
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
