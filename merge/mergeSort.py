import timeit
import random

random_array = []
sorted_array = []
reverse_sorted_array = []


def fill_random_array():
    return [random.randint(1, 50000) for _ in range(50000)]


def fill_sorted_array():
    for i in range(0, 50000):
        sorted_array.append(i)


def fill_reverse_sorted_array():
    for i in range(0, 50000):
        reverse_sorted_array.append(50000 - i)


def merge(left, right):
    sorted_l = []
    left_index = right_index = 0

    left_length, right_length = len(left), len(right)

    for _ in range(left_length + left_length):
        if left_index < left_length and right_index < left_length:

            # if left[left_index] >= right[right_index]: from max to min
            if left[left_index] <= right[right_index]:
                sorted_l.append(left[left_index])
                left_index += 1


            else:
                sorted_l.append(right[right_index])
                right_index += 1

        elif left_index == left_length:
            sorted_l.append(right[right_index])
            right_index += 1

        elif right_index == left_length:
            sorted_l.append(left[left_index])
            left_index += 1

    return sorted_l


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_l = merge_sort(nums[:mid])
    right_l = merge_sort(nums[mid:])
    return merge(left_l, right_l)


random_array = fill_random_array()
fill_sorted_array()
fill_reverse_sorted_array()
tDown = timeit.timeit(lambda: merge_sort(random_array), number=1)
print("random array: ", round(tDown, 6))
t_Ms_S = timeit.timeit(lambda: merge_sort(sorted_array), number=1)
print("sorted array:   ", round(t_Ms_S, 6))
t_Ms_RS = timeit.timeit(lambda: merge_sort(reverse_sorted_array), number=1)
print("reverse: ", round(t_Ms_RS, 6))
