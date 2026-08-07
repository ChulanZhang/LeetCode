class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use hashtable to record the num and how mant times they appear in the array
        nums_hashtable = {}
        for num in nums:
            if num in nums_hashtable.keys():
                return True
            else:
                nums_hashtable[num] = 1
        return False
        