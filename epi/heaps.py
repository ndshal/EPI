import heapq

def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_entry_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_entry_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_entry_i))

    return result
