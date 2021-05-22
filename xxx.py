# import timeit
# import random
#
#
# arrRand = []
# arrSort = []
# arrRSort = []
#
#
# def randArr():
#     return [random.randint(1, 100000) for _ in range(100000)]
#
#
# def sortArr():
#     for i in range(0, 100000):
#         arrSort.append(i)
#
#
# def sortRArr():
#     for i in range(0, 100000):
# arrRSort.append(100000 - i)
#
#
# def part(arr, loI, hiI):
#     #arr[loI], arr[(loI + hiI) // 2] = arr[(loI + hiI) // 2], arr[loI]
#     pivot = arr[loI]
#     i = loI + 1
#     for j in range(loI + 1, hiI + 1):
#         if arr[j] < pivot:
#             arr[j], arr[i] = arr[i], arr[j]
#             i += 1
#     arr[i - 1], arr[loI] = arr[loI], arr[i - 1]
#     return i - 1
#
#
# def qs(arr, loI, hiI):
#     if loI < hiI:
#         pivot = part(arr, loI, hiI)
#         qs(arr, loI, pivot - 1)
#         qs(arr, pivot + 1, hiI)
#
#
# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#
#     if l < n and arr[largest] < arr[l]:
#         largest = l
#
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
#
# def heapSort(arr):
#     n = len(arr)
#
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
#
# # -----
#
# def bubbleSort(arr):
#     for i in range(len(arr)):
#         low = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[low]:
#                 low = j
#         arr[i], arr[low] = arr[low], arr[i]
#
#
# # arrRand = randArr()
# sortArr()
# sortRArr()
# tQsR = timeit.timeit(lambda: qs(arrRand, 0, len(arrRand) - 1), number=1)
# tQsS = timeit.timeit(lambda: qs(arrSort, 0, len(arrSort) - 1), number=1)
# tQsRS = timeit.timeit(lambda: qs(arrRSort, 0, len(arrRSort) - 1), number=1)
#
# print("QS random: ", round(tQsR, 6))
# print("QS sort:   ", round(tQsS, 6))
# print("QS r sort: ", round(tQsRS, 6))
#
# arrRand = randArr()
# sortArr()
# sortRArr()
# tHepR = timeit.timeit(lambda: heapSort(arrRand), number=1)
# tHepS = timeit.timeit(lambda: heapSort(arrSort), number=1)
# tHepRS = timeit.timeit(lambda: heapSort(arrRSort), number=1)
#
# print("HS random: ", round(tHepR, 6))
# print("HS sort:   ", round(tHepS, 6))
# print("HS r sort: ", round(tHepRS, 6))
#
# arrRand = randArr()
# sortArr()
# sortRArr()
# tBsR = timeit.timeit(lambda: bubbleSort(arrRand), number=1)
# tBsS = timeit.timeit(lambda: bubbleSort(arrSort), number=1)
# tBsRS = timeit.timeit(lambda: bubbleSort(arrRSort), number=1)
#
# print("BS random: ", round(tBsR, 6))
# print("BS sort:   ", round(tBsS, 6))
# print("BS r sort: ", round(tBsRS, 6))
