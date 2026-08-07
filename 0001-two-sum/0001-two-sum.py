class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashtable = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_hashtable.keys():
                return [nums_hashtable[diff], i]
            else:
                nums_hashtable[num] = i