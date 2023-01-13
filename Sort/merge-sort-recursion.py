def merge_sort(arr):
    if len(arr)<1:
        return arr
    else:
        mid = len(arr)//2
        return merge_sort([i for i in arr[:mid]]) + merge_sort([j for j in arr[mid:]])

print(merge_sort([9,8,7,6,5,4,3,2]))