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


arrRand = fillRandArr()
fillSortArr()
fillSortRArr()
tDown = timeit.timeit(lambda: merge_sort(arrRand), number=1)
print("BS random: ", round(tDown, 6))
tQsS = timeit.timeit(lambda: merge_sort(arrSort), number=1)
print("BS sort:   ", round(tQsS, 6))
tQsRS = timeit.timeit(lambda: merge_sort(arrRSort), number=1)
print("BS r sort: ", round(tQsRS, 6))
