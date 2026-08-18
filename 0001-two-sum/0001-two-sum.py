class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a hashmap to store the prior number and index
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap.keys():
                return [hashmap[diff], i]
            else:
                hashmap[num] = i