def issorted(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    return arr[0] <= arr[1] and issorted(arr[1:])


print(issorted([1, 3, 4, 5, 6, 7]))
