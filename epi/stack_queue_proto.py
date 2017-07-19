import collections

class Stack:
    """LIFO stack with max API"""

    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax',
                                                  ('element', 'max'))
    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        cached_max = x if self.empty() else max(x, self.max())

        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, cached_max))

class Queue:
    """Ring-buffer style circular queue"""
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0

    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries):
            self.resize()
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('dequeue(): empty queue')
        self._num_queue_elements -= 1
        el = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        return el

    def size(self):
        return self._num_queue_elements

    def resize(self):
        self._entries = (
            self._entries[self._head:] + self._entries[:self._head])
        self._head, self._tail = 0, self._num_queue_elements
        self._entries += [None] * (len(self._entries) * Queue.SCALE_FACTOR)
