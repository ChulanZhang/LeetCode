class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                prefix[i] = prefix[i - 1] + 1
        
        for j in range(n - 2, -1, -1):
            if nums[j] <= nums[j + 1]:
                suffix[j] = suffix[j + 1] + 1
        
        max_subarray_length = max(prefix)
        for i in range(n):
            left = prefix[i - 1] if i > 0 else 0
            right = suffix[i + 1] if i < n - 1 else 0
            if i > 0 and i < n - 1 and nums[i - 1] <= nums[i + 1]:
                max_subarray_length = max(max_subarray_length, left + right + 1)
            else:
                max_subarray_length = max(max_subarray_length, max(left, right) + 1)
        return max_subarray_length