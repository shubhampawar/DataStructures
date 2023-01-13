class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0

        for j in range(l):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                # print(nums)
