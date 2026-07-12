class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numMap.keys():
                return [numMap[diff], i]
            else:
                numMap[num] = i
        