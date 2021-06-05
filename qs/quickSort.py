import timeit
import random


random_array_2 = []
sorted_array_2 = []
reverse_sorted_array_2 = []


def fill_random_array():
    return [random.randint(1, 50000) for _ in range(50000)]


def fill_sorted_array():
    for i in range(0, 50000):
        sorted_array_2.append(i)


def fill_reverse_sorted_array():
    for i in range(0, 50000):
        reverse_sorted_array_2.append(50000 - i)


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


random_array_2 = fill_random_array()
fill_sorted_array()
fill_reverse_sorted_array()
tDown = timeit.timeit(lambda: quicksort(random_array_2, 0, len(random_array_2) - 1), number=1)
print("random time: ", round(tDown, 6))
tQsS = timeit.timeit(lambda: quicksort(sorted_array_2, 0, len(sorted_array_2) - 1), number=1)
print("sort time:   ", round(tQsS, 6))
tQsRS = timeit.timeit(lambda: quicksort(reverse_sorted_array_2, 0, len(reverse_sorted_array_2) - 1), number=1)
print("reverse sort time: ", round(tQsRS, 6))

