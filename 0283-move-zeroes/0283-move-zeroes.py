class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_avail_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[first_avail_idx] = nums[first_avail_idx], nums[i]
                first_avail_idx += 1
        
        