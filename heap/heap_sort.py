import random
from adt import MaxHeap


def heap_sort(arr):
    m = MaxHeap()
    result = []
    for i in arr:
        m.add(i)
    for _ in range(len(arr)):
        result.append(m.extract())
    return result


def test_heapsort_reverse():
    ll = list(range(10))
    random.shuffle(ll)
    assert heap_sort(ll) == sorted(ll, reverse=True)


if __name__ == "__main__":
    test_heapsort_reverse()
