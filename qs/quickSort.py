import timeit


def partition(arr, min_index, max_index):
    p = min_index
    pivot = arr[max_index]
    for i in range(min_index, max_index):
        # if arr[i] >= pivot: from max to min
        if arr[i] <= pivot:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
    arr[p], arr[max_index] = arr[max_index], arr[p]
    return p


def quicksort(arr, min_index, max_index):
    if min_index < max_index:
        q = partition(arr, min_index, max_index)
        quicksort(arr, min_index, q - 1)
        quicksort(arr, q + 1, max_index)


xxx = [35, 12, 43, 8, 51, 44, 78, 1, 17, 55, 100, 3, 19, 25, 11, 22, 2, 99]
tDown = timeit.timeit(lambda: quicksort(xxx, 0, len(xxx) - 1), number=100)
print(tDown)
# tUp = timeit.timeit(lambda: quicksort(xxx, 0, len(xxx) - 1), number=100)
# print(tUp)
print(xxx)
