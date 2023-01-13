def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    temp = []
    for i in range(l):
        newplace = (i + k) % l
        temp.insert(newplace,nums[i])
    print(temp)

rotate([1,2,3,4,5,6,7],3)