from os import *
from sys import *
from collections import *
from math import *


def getpivot(arr, n):
    s, e = 0, n - 1
    mid = (s + e) // 2
    while (s < e):
        if arr[mid] > arr[0]:
            s = mid + 1
        else:
            e = mid
        mid = (s + e) // 2
    return s


def binSearch(arr, s, e, k):
    #     print(arr, s, e, k)
    s = s
    e = e
    mid = (s + e) // 2

    while s < e:
        #         print(mid)
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            e = mid - 1
        else:
            s = mid + 1
        mid = s - (s + e) // 2
    return -1


def findPosition(arr, n, k):
    pivot = getpivot(arr, n)
    if arr[pivot] <= k <= arr[n - 1]:
        # print(pivot,n-1,k)
        return binSearch(arr, pivot, n - 1, k)
    else:
        return binSearch(arr, 0, pivot - 1, k)


# print(findPosition([2,4,5,6,8,9,1], 7, 2))

print(findPosition([4, 5, 6, 7, 0, 1, 2], 7, 0))
assert findPosition([4, 5, 6, 7, 0, 1, 2], 7, 0) == 4
