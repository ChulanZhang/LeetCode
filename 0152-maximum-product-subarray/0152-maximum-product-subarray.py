class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_product stores the maximum product
        # found anywhere in the array so far.
        #
        # We initialize it with nums[0] because
        # the subarray must contain at least one element.
        max_product = nums[0]
        # max_sum means:
        # the maximum subarray sum we have seen anywhere so far.
        #
        # We also initialize it with nums[0] so that arrays
        # containing only negative numbers are handled correctly.
        curr_min = nums[0]
        curr_max = nums[0]
        for i in range(1, len(nums)):
            temp = curr_max
            # For the maximum product ending at index i,
            # we have three choices:
            #
            # 1. Start a new subarray from nums[i]
            #       num
            #
            # 2. Extend the previous maximum-product subarray
            #       previous_max * num
            #
            # 3. Extend the previous minimum-product subarray
            #       previous_min * num
            #
            # Choice 3 is important when num is negative:
            # negative * negative can become a large positive value.
            curr_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            # Similarly, we also keep track of the minimum product
            # ending at the current position.
            #
            # A very negative product may become useful later
            # if another negative number appears.
            curr_min = min(nums[i], nums[i] * temp, nums[i] * curr_min)
            # current_max is only the best product that ENDS
            # at the current index.
            #
            # max_product stores the best answer across
            # ALL positions seen so far.
            max_product = max(max_product, curr_max)
        return max_product
        