from timeit import default_timer as timer
from datetime import timedelta


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
    start = timer()
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    end = timer()
    print(timedelta(seconds=end - start))
    return merge(left, right)


random_numbers = [35, 12, 43, 8, 51, 44, 78, 1, 17, 55, 100, 3, 19, 25, 11, 22, 2, 99]
random_numbers = merge_sort(random_numbers)
print(random_numbers)
