import timeit
import random


# arrRand = []
# arrSort = []
# arrRSort = []
#
#
# def fillRandArr():
#     return [random.randint(1, 50000) for _ in range(50000)]
#
#
# def fillSortArr():
#     for i in range(0, 50000):
#         arrSort.append(i)
#
#
# def fillSortRArr():
#     for i in range(0, 50000):
#         arrRSort.append(50000 - i)


def partition(arr, min_index, max_index):
    arr[min_index], arr[(min_index + max_index) // 2] = arr[(min_index + max_index) // 2], arr[min_index]
    pivot = arr[min_index]
    p = min_index + 1
    for i in range(min_index + 1, max_index + 1):
        # if arr[i] >= pivot: from max to min
        if arr[i] < pivot:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1

    arr[p - 1], arr[min_index] = arr[max_index], arr[p - 1]
    return p - 1


def quicksort(arr, min_index, max_index):
    if min_index < max_index:
        q = partition(arr, min_index, max_index)
        quicksort(arr, min_index, q - 1)
        quicksort(arr, q + 1, max_index)


# arrRand = fillRandArr()
# fillSortArr()
# fillSortRArr()
# tDown = timeit.timeit(lambda: quicksort(arrRand, 0, len(arrRand) - 1), number=1)
# print("BS random: ", round(tDown, 6))
# tQsS = timeit.timeit(lambda: quicksort(arrSort, 0, len(arrSort) - 1), number=1)
# print("BS sort:   ", round(tQsS, 6))
# tQsRS = timeit.timeit(lambda: quicksort(arrRSort, 0, len(arrRSort) - 1), number=1)
# print("BS r sort: ", round(tQsRS, 6))

