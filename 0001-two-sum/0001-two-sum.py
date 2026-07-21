class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numsMap.keys():
                return [numsMap[diff], i]
            else:
                numsMap[num] = i
        