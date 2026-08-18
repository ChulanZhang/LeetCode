class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # we can do one pass and record the sum of every subarray and their index, if we find a same sum, we return true
        sum_map = set()
        for i in range(len(nums) - 1):
            subarray_sum = nums[i] + nums[i + 1]
            if subarray_sum in sum_map:
                return True
            else:
                sum_map.add(subarray_sum)
        return False  