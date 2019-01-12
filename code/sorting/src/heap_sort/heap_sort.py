# Part of Cosmos by OpenGenus Foundation
import math
from datastructures.src.tree.heap import max_heap


def __swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


# sorting is in the ascending order
def heap_sort(arr):
    # form a max heap
    # for i in range(math.floor(len(arr) / 2), -1, -1):
    #     heap_root(arr, i, len(arr))
    max_heap.build_max_heap(arr)

    length = len(arr)
    # remove the root and reform the heap
    for i in range(len(arr) - 1, 0, -1):
        __swap(arr, 0, i)
        length -= 1
        max_heap.heapify(arr, 0, length)
