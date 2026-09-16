class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first_num = float('inf')
        second_num = float('inf')
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False

# nums = [2,1,5,0,4,6]
# f = 2
# f = 1
# s = 5
# f = 0
# s = 4
# third = 6, return True

# nums = [2,1,5,0,0,6]
# f = 2
# f = 1
# s = 5
# f = 0
# f = 0
# third = 6, return True

# TC: O(n)
# SC: O(1)