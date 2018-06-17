# Part of Cosmos by OpenGenus Foundation

class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def empty(self):
        return len(self) == 0

    def clear(self):
        self._data = []

    def push(self, x):
        self._data.insert(0, x)

    def pop(self):
        self._data.pop()

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

    q.push(1)
    q.push(1)
    q.push(1)
    assert(not q.empty())
    q.clear()
    assert(q.empty())

if __name__ == "__main__":
    main()
