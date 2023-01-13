def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = j = k = 0

    while (i < m and j < n):
        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
            i += 1

        else:
            nums2[j], nums1[i] = nums1[i], nums2[j]
            j += 1

    while (j < n):
        nums1.append(nums2[j])

    # while(i<m):
    #     nums1.append(nums1[i])

    return nums1


print(merge([7, 6, 5, 4, 0, 0, 0], 7, [3, 4, 5, 6], 4))
