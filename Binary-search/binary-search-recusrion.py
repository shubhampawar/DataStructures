def issorted(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    return arr[0] <= arr[1] and issorted(arr[1:])


def search(arr, k, idx):
    if issorted(arr) and len(arr) > 1:
        print(arr)
        if arr[0] == k:
            return True,idx
        else:
            return search(arr[1:], k, idx + 1)


print(search([1, 2, 3, 4, 5, 6, 7], 8, 0))
