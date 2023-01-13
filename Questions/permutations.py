def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def solve(a, l, r, ans):
    if l == r:
        ans.append(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            solve(a, l + 1, r, ans)
            a[l], a[i] = a[i], a[l]


def permutaion(arr):
    ans = []
    index = 0
    l = len(arr)
    solve(arr, index, l, ans)
    return ans


print(permutaion([1, 2, 3]))
