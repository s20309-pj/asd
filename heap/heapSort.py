import timeit
import random

arrRand = []
arrSort = []
arrRSort = []


def fillRandArr():
    return [random.randint(1, 50000) for _ in range(50000)]


def fillSortArr():
    for i in range(0, 50000):
        arrSort.append(i)


def fillSortRArr():
    for i in range(0, 50000):
        arrRSort.append(50000 - i)


def heapify(numbers, heap_size, index):
    maximum = index
    left_side = (2 * index) + 1
    right_side = (2 * index) + 2

    if left_side < heap_size and numbers[left_side] > numbers[maximum]:
        maximum = left_side

    if right_side < heap_size and numbers[right_side] > numbers[maximum]:
        maximum = right_side

    if maximum != index:
        numbers[index], numbers[maximum] = numbers[maximum], numbers[index]
        # Heapify the new root element to ensure it's the largest
        heapify(numbers, heap_size, maximum)


def heap_sort(numbers):
    n = len(numbers)

    for i in range(n, -1, -1):
        # Swap
        heapify(numbers, n, i)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]

        heapify(numbers, i, 0)


arrRand = fillRandArr()
fillSortArr()
fillSortRArr()
tDown = timeit.timeit(lambda: heap_sort(arrRand), number=1)
print("BS random: ", round(tDown, 6))
tQsS = timeit.timeit(lambda: heap_sort(arrSort), number=1)
print("BS sort:   ", round(tQsS, 6))
tQsRS = timeit.timeit(lambda: heap_sort(arrRSort), number=1)
print("BS r sort: ", round(tQsRS, 6))
