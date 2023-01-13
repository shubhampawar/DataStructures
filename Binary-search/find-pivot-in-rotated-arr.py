'''

[1,2,3,4,5,6,7]

[3,4,5,6,7,          1,2]
'''


def search(arr, arr_rot):
    l = len(arr)  # 7
    s, e = 0, l - 1  # 0 , 6
    mid = (s + e) // 2  # 3

    while (s < e):  # 0 < 6

        if arr[mid] > arr[0]:  # 2 > 6
            s = mid + 1
        else:
            e = mid  # e = 3
        mid = (s + e) // 2

    return s


print(search([5, 6, 7, 1, 2, 3, 4], [1, 2, 3, 4, 5, 6]))
