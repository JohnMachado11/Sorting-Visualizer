
from random import randint


def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]

    print(arr)

nums = [randint(0,100) for i in range(100)]

# print(nums)

# nums = randrange()

bubble_sort(nums)