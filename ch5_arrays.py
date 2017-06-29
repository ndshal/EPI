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

def main():
    print 'even_odd([1, 2, 3, 4, 5]) == [4, 2, 3, 5, 1]:', even_odd([1, 2, 3, 4, 5]) == [4, 2, 3, 5, 1]

if __name__ == '__main__':
    main()
