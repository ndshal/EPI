def bsearch(A, t):
    """Iterative binary search for t"""
    left, right = 0, len(A) - 1
    while left <= right:
        mid = left + (right - left) // 2 #(L+U)/2 could cause overflow
        if A[mid] < t:
            left = mid + 1
        elif A[mid] == t:
            return mid
        else:
            right = mid - 1

    return -1

def search_first_of_k(A, k):
    """Return the index of the first occurence of k in A (or -1)"""
    return -1
