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

# call A[i] the pivot, partition the array so that
# A[j] < A[i] and A[k] >= A[i] for j < i and k > i respectively
def dutch_flag_partition(A, i):
    return A
