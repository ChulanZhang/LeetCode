from typing import List, Optional, Dict, Set

# 3Sum (三数之和) - Medium
# 🔑 核心考点: 双指针 (Two Pointers) / 排序 (Sorting)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     暴力搜索三个数，时间复杂度为 O(N^3)，且去重逻辑极其繁琐。如何进行优化并去重？
#   - 思维推导: 
#     1. 首先对数组进行升序排序，这是使用双指针的前提。
#     2. 固定第一个数 nums[i]，如果 nums[i] > 0 则后面不可能凑出 0，直接终止。如果 nums[i] == nums[i-1] 则跳过以去重。
#     3. 在剩下的区间 [i+1, n-1] 中使用双指针 left 和 right 向中间夹逼。若三数之和小于 0 则 left += 1，大于 0 则 right -= 1。若等于 0，则记录答案，并移动双指针同时跳过重复的值去重。

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

