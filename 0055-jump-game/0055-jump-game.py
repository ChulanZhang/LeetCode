class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach_index = 0
        for curr_index, curr_max_jump in enumerate(nums):
            if curr_index > max_reach_index:
                return False
            max_reach_index = max(max_reach_index, curr_index + curr_max_jump)
        return True

        # goal = len(nums) - 1
        # for curr_index, curr_jump in enumerate(len(nums) - 1, -1, -1):
        #     if curr_index + curr_jump >= goal:
        #         goal = curr_index
        # return goal == 0

        # Solution 1
        # Greedy
        # max_reach >= len(nums) -1
        # nums = [2, 2, 1, 0, x, x, ......], index of x is 4
        # nums = [3,2,1,0,4,5,6]
        # max_reach = 0, max_reach = max(0, 0 + 3) = 3
        # max_reach = 3, max_reach = max(3, 1 + 2) = 3
        # max_reach = 3, max_reach = max(3, 2 + 1) = 3
        # max_reach = 3, max_reach = max(3, 3 + 0) = 3
        # max_reach = 3, curr_index = 4
        # max_reach_index = 0
        # for curr_index, curr_steps in enumerate(nums):
        #     if curr_index > max_reach_index:
        #         return False
        #     max_reach_index = max(max_reach_index, curr_index + curr_steps)
        #     # max_reach = max(0, 0 + 3)
        # return True
        # TC: O(n) for one for loop
        # SC: O(1)

        # Solution 2
        # The idea is to traversing backwards
        # goal is the position we want to reach
        # goal = len(nums) - 1
        # for i in range(len(nums) - 1, -1, -1):
        #     if i + nums[i] >= goal:
        #         goal = i
        # return goal == 0
        # TC: O(n)
        # SC: O(1)

        