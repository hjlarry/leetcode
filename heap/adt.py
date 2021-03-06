class MaxHeap:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize or 32
        self._elements = [None] * self.maxsize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, item):
        if self._count >= self.maxsize:
            raise Exception("full heap")
        self._elements[self._count] = item
        self._count += 1
        self._sift_up(self._count - 1)

    def _sift_up(self, cur):
        if cur > 0:
            parent = int((cur - 1) / 2)
            if self._elements[cur] > self._elements[parent]:
                self._elements[cur], self._elements[parent] = (
                    self._elements[parent],
                    self._elements[cur],
                )
                self._sift_up(parent)

    def extract(self):
        if self._count < 1:
            raise Exception("empty heap")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._sift_down(0)
        return value

    def _sift_down(self, cur):
        left = 2 * cur + 1
        right = 2 * cur + 2
        largest = cur
        if (
            left < self._count
            and self._elements[left] > self._elements[cur]
            and self._elements[left] > self._elements[right]
        ):
            largest = left
        elif right < self._count and self._elements[right] > self._elements[cur]:
            largest = right

        if largest != cur:
            self._elements[cur], self._elements[largest] = (
                self._elements[largest],
                self._elements[cur],
            )
            self._sift_down(largest)


def test_maxheap():
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    for i in reversed(range(n)):
        assert i == h.extract()


class MinHeap:
    # 和最大堆相比，只是在_sift_up和_sift_down时的比较判断不同
    def __init__(self, maxsize=None):
        self.maxsize = maxsize or 32
        self._elements = [None] * self.maxsize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, item):
        if self._count >= self.maxsize:
            raise Exception("full heap")
        self._elements[self._count] = item
        self._count += 1
        self._sift_up(self._count - 1)

    def _sift_up(self, cur):
        if cur > 0:
            parent = int((cur - 1) / 2)
            if self._elements[cur] < self._elements[parent]:
                self._elements[cur], self._elements[parent] = (
                    self._elements[parent],
                    self._elements[cur],
                )
                self._sift_up(parent)

    def extract(self):
        if self._count < 1:
            raise Exception("empty heap")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._sift_down(0)
        return value

    def _sift_down(self, cur):
        left = 2 * cur + 1
        right = 2 * cur + 2
        smallest = cur
        if (
            left < self._count
            and self._elements[left] < self._elements[cur]
            and self._elements[left] < self._elements[right]
        ):
            smallest = left
        elif right < self._count and self._elements[right] < self._elements[cur]:
            smallest = right

        if smallest != cur:
            self._elements[cur], self._elements[smallest] = (
                self._elements[smallest],
                self._elements[cur],
            )
            self._sift_down(smallest)


def test_minheap():
    n = 5
    h = MinHeap(n)
    for i in range(n):
        h.add(i)
    for i in range(n):
        assert i == h.extract()


if __name__ == "__main__":
    test_maxheap()
    test_minheap()
