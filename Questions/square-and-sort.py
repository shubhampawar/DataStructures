def square(arr):
    return [i * i for i in arr]


def q_sort(arr):
    if len(arr) <= 1:
        return arr
    return q_sort([i for i in arr[1:] if i <= arr[0]]) + [arr[0]] + q_sort([j for j in arr[:1] if j > arr[0]])


def sol():
    arr = [9, 8, 7, 6, 5, 3, 2, 1]

    sq = square(arr)
    print(sq)
    srt = q_sort(sq)
    print(srt)


sol()
