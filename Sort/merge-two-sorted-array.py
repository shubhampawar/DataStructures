def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = j = k = 0
    nums = []
    while (i < m and j < n):
        if nums1[i] < nums2[j]:
            # nums1[i],nums2[j] = nums2[j],nums1[i]
            print(i,j)
            nums.append(nums1[i])
            i += 1
            k += 1
        else:
            nums.append(nums2[j])
            j += 1
            k += 1
    while i < m:
        nums.append(nums1[i])
        k += 1
        i += 1
    while j < n:
        nums.append(nums2[j])
        k += 1
        j += 1
    nums1 = nums
    print(nums1)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
'''
[1, 2, 3, 0, 0, 0]

[2, 5, 6]

'''