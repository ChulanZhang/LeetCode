class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            sum_d = 0
            while num >= 10:
                sum_d += num%10
                num = num // 10
            sum_d += num

            if sum_d == i:
                return i
        return -1

# TC: O(N*k)
# 
        