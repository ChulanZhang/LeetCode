class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # max_sum means:
        # the maximum subarray sum we have seen anywhere so far.
        #
        # We initialize it with nums[0] so that arrays
        # containing only negative numbers are handled correctly.
        max_sum = nums[0]
        # current_sum means:
        # the maximum subarray sum that MUST end at the current index.
        #
        # We initialize it with nums[0] because the subarray
        # must contain at least one element.
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

        