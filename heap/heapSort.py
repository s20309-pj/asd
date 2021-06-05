import timeit
import random

random_array_3 = []
sorted_array_3 = []
reverse_sorted_array_3 = []


def fill_random_array_3():
    return [random.randint(1, 50000) for _ in range(50000)]


def fill_sorted_array_3():
    for i in range(0, 50000):
        sorted_array_3.append(i)


def fill_reverse_sorted_array_3():
    for i in range(0, 50000):
        reverse_sorted_array_3.append(50000 - i)


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
        heapify(numbers, heap_size, maximum)


def heap_sort(numbers):
    n = len(numbers)

    for i in range(n, -1, -1):

        heapify(numbers, n, i)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]

        heapify(numbers, i, 0)


random_array_3 = fill_random_array_3()
fill_sorted_array_3()
fill_reverse_sorted_array_3()
tDown = timeit.timeit(lambda: heap_sort(random_array_3), number=1)
print("random time: ", round(tDown, 6))
t_Hs_S = timeit.timeit(lambda: heap_sort(sorted_array_3), number=1)
print("sort time:   ", round(t_Hs_S, 6))
t_Hs_RS = timeit.timeit(lambda: heap_sort(reverse_sorted_array_3), number=1)
print("reverse sort time: ", round(t_Hs_RS, 6))
