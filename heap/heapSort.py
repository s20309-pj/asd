import timeit


def heapify(numbers, heap_size, index):
    maximum = index
    left_side = (2 * index) + 1
    right_side = (2 * index) + 2

    # if left_side < heap_size and numbers[left_side] < numbers[maximum]: from max to min
    if left_side < heap_size and numbers[left_side] > numbers[maximum]:
        maximum = left_side

    # if right_side < heap_size and number[right_side] < numbers[maximum]: from max to min
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


random_numbers = [35, 12, 43, 8, 51, 44, 78, 1, 17, 55, 100, 3, 19, 25, 11, 22, 2, 99]
# tDown = timeit.timeit(lambda: heap_sort(random_numbers), number=100)
# print(tDown)
tUp = timeit.timeit(lambda: heap_sort(random_numbers), number=100)
print(tUp)
heap_sort(random_numbers)
print(random_numbers)
