class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        prefix_sum = 0
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            if prefix_sum in hashmap:
                curr_length = i - hashmap[prefix_sum]
                max_length = max(max_length, curr_length)
            else:
                hashmap[prefix_sum] = i
        
        return max_length
        