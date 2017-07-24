import csv
import heapq
import itertools

def merge_sorted_arrays(sorted_arrays):
    """Merge sorted arrays in less than nlog(n) time"""
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

def sort_k_sorted_array(sequence, k):
    """Sort an array where no element is more than k away from its correct pos"""
    min_heap = []
    result = []

    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    for x in sequence[k:]:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result

class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return self.x**2 + self.y**2 + self.z**2

    def __lt__(self, other_star):
        return self.distance < other_star.distance

def find_k_closest_stars(k, stars):
    max_heap = []
    reader = csv.reader(stars)
    for line in reader:
        star = Star(*map(float, line))
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    return [s[1] for s in heapq.nlargest(k, max_heap)]
