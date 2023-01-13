def partition(arr, s, e):
    pivot = arr[e]
    i = s - 1
    for j in range(s, e):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(arr, 1)
    arr[i + 1], arr[e] = arr[e], arr[i + 1]
    return i + 1


def quicksort(arr, s, e):
    print(arr)
    if s < e:
        pivot = partition(arr, s, e)
        quicksort(arr, s, pivot - 1)
        quicksort(arr, pivot + 1, e)


arr = [4, 1, 2, 7, 6, 9, 8]
n = len(arr)
quicksort(arr, 0, n - 1)

print(arr)
