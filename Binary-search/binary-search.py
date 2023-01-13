def search(arr, n):
    print(arr)
    l = len(arr)
    start = 0
    end = l
    mid = (start + end) // 2

    while (start <= end):
        print(f"start {start},end {end},mid {mid}")
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
        mid = start+(end-start) // 2


print(search([i for i in range(100)], 10))
