# Part of Cosmos by OpenGenus Foundation
class Queue:
    def __init__(self):
        self._size = 0
        self._data = []

    def empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def push(self, x):
        self._data.insert(0, x)
        self._size += 1

    def pop(self):
        if self._size == 0:
            return None
        x = self._data.pop()
        self._size -= 1

    def front(self):
        return self.data()[0]

    def back(self):
        return self.data()[-1]

    def data(self):
        return self._data[::-1]


def main():
    q = Queue()
    assert(q.data() == [])
    assert(q.empty())
    assert(len(q) == 0)

    q.push(1)
    assert(q.data() == [1])
    assert(q.front() == 1)
    assert(q.back() == 1)
    assert(not q.empty())
    assert(len(q) == 1)

    q.push(2)
    assert(q.data() == [1, 2])
    assert(q.front() == 1)
    assert(q.back() == 2)
    assert(not q.empty())
    assert(len(q) == 2)

    q.pop()
    assert(q.data() == [2])
    assert(q.front() == 2)
    assert(q.back() == 2)
    assert(not q.empty())
    assert(len(q) == 1)

    q.push(3)
    assert(q.data() == [2, 3])
    assert(q.front() == 2)
    assert(q.back() == 3)
    assert(not q.empty())
    assert(len(q) == 2)

    q.pop()
    assert(q.data() == [3])
    assert(q.front() == 3)
    assert(q.back() == 3)
    assert(not q.empty())
    assert(len(q) == 1)

    q.pop()
    assert(q.data() == [])
    assert(q.empty())
    assert(len(q) == 0)

if __name__ == "__main__":
    main()
