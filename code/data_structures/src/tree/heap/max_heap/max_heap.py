# Part of Cosmos by OpenGenus Foundation
def __left(i):
    return 2 * i + 1


def __right(i):
    return 2 * i + 2


def heapify(a, root, length=None):
    if length is None:
        length = len(a)
    l = __left(root)
    r = __right(root)
    largest = root

    if l < length and a[l] > a[largest]:
        largest = l
    if r < length and a[r] > a[largest]:
        largest = r

    if largest != root:
        a[root], a[largest] = a[largest], a[root]
        heapify(a, largest, length)


def build_max_heap(a):
    for i in range((len(list(a)) - 1) // 2, -1, -1):
        heapify(a, i)
