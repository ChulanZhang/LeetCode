class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        curr_min = nums[0]
        curr_max = nums[0]
        for i in range(1, len(nums)):
            temp = curr_max
            curr_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_min = min(nums[i], nums[i] * temp, nums[i] * curr_min)
            max_product = max(max_product, curr_max)
        return max_product
        