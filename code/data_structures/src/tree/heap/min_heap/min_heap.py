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
    smallest = root

    if l < length and a[l] < a[smallest]:
        smallest = l
    if r < length and a[r] < a[smallest]:
        smallest = r

    if smallest != root:
        a[root], a[smallest] = a[smallest], a[root]
        heapify(a, smallest, length)


def build_min_heap(a):
    for i in range((len(list(a)) - 1) // 2, -1, -1):
        heapify(a, i)
