class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_len = 1
                while curr_num + 1 in nums_set:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
        
        return max_len
        # longest_streak = 0
        # num_set = set(nums)

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_num = num
        #         current_streak = 1

        #         while current_num + 1 in num_set:
        #             current_num += 1
        #             current_streak += 1

        #         longest_streak = max(longest_streak, current_streak)

        # return longest_streak
        