# Array category data
PROBLEMS = {
    "01_two_sum.py": {
        "title": "Two Sum (两数之和)",
        "difficulty": "Easy",
        "key_points": "哈希表 (Hash Map) - 空间换时间",
        "analysis_intuition": "最容易想到的暴力方法是双重循环（Nested Loops），外层固定元素 A，内层在其余元素中寻找 B 使得 A + B = target。时间复杂度是 O(N^2)。在面试中是无法接受的，尤其是当数组规模达到 10^4 以上时，会直接超时。且要注意避开同一个元素重复使用和重复数值的处理这两个边界。",
        "analysis_derivation": "为了将复杂度降低到 O(N)，我们需要在一边遍历数组的过程中，一边把已经访问过的元素及其索引存入哈希表中。这样，对于下一个数，我们只需在哈希表中检索它的互补数是否存在即可。利用哈希表进行 O(1) 复杂度的查找。",
        "code": """from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            num_to_idx[num] = i
        return []
"""
    },
    "02_best_time_to_buy_and_sell_stock.py": {
        "title": "Best Time to Buy and Sell Stock (买卖股票的最佳时机)",
        "difficulty": "Easy",
        "key_points": "贪心算法 (Greedy) / 动态规划状态简化 - 一次遍历",
        "analysis_intuition": "暴力解法是计算所有可能的买入和卖出组合（即双重循环，外层买入，内层卖出且卖出在买入之后），寻找最大的差值，时间复杂度为 O(N^2)。",
        "analysis_derivation": "由于你必须先买入，才能卖出，不能简单地找出数组的最小值和最大值然后相减（因为最大值可能出现在最小值之前）。我们在遍历数组时，可以实时维护一个“历史最低买入价” min_price，以及“历史最大利润” max_profit。当我们在第 i 天卖出股票，最大利润就是价格差 price - min_price。我们用它去更新 max_profit 即可。",
        "code": """from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
"""
    },
    "03_contains_duplicate.py": {
        "title": "Contains Duplicate (存在重复元素)",
        "difficulty": "Easy",
        "key_points": "哈希集合 (Hash Set) - 早期终止优化",
        "analysis_intuition": "暴力解法是双重循环，依次两两比对，时间复杂度为 O(N^2)。如果直接使用 Python 的 len(set(nums)) != len(nums)，大数组下，无法早期终止（Early Return）可能会导致不必要的性能浪费。",
        "analysis_derivation": "在允许使用额外空间的前提下，为了达到 O(N) 的时间复杂度，我们可以使用哈希集合 visited。一边遍历数组，一边把遇到的数字放入 visited 中。每次放入前先检查它是否已经在 visited 中。如果在，说明找到了重复元素，直接返回 True 早期终止。",
        "code": """from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
"""
    },
    "04_product_of_array_except_self.py": {
        "title": "Product of Array Except Self (除自身以外数组的乘积)",
        "difficulty": "Medium",
        "key_points": "前缀乘积与后缀乘积 (Prefix & Suffix Products) / 空间优化",
        "analysis_intuition": "最直观的方法是把所有数乘起来得到 total_product，然后除以每个位置的 nums[i]。但题目要求不能使用除法，且如果数组中包含 0 会导致除以 0 的错误。",
        "analysis_derivation": "除了自身之外的所有元素积，可以拆分为：当前元素左边所有数的乘积（前缀积）乘上右边所有数的乘积（后缀积）。我们可以直接用返回的 answer 数组暂存前缀积。接着，反向扫描数组，用一个变量 suffix_product 动态维护右侧乘积，并在遍历过程中乘到对应的位置上，这样实现 O(1) 额外空间。",
        "code": """from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
        return answer
"""
    },
    "05_maximum_subarray.py": {
        "title": "Maximum Subarray (最大子数组和)",
        "difficulty": "Medium",
        "key_points": "动态规划 (Kadane's Algorithm) / 贪心算法",
        "analysis_intuition": "暴力枚举所有的子数组起点 i 和终点 j，时间复杂度为 O(N^2)。如果数组中全为负数，初始化最大值需要注意不能直接设为 0，必须设为首个元素或负无穷。",
        "analysis_derivation": "在遍历到每个位置时，我们需要决定：是要继续累加当前数字，还是以当前数字为新子数组的起点？如果之前的累加和为负数，对后续累加只会起到削减作用，应当舍弃并从当前数重新开始。状态转移方程为：current_sum = max(num, current_sum + num)。并在过程中维护全局最大值。",
        "code": """from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
"""
    },
    "06_maximum_product_subarray.py": {
        "title": "Maximum Product Subarray (乘积最大子数组)",
        "difficulty": "Medium",
        "key_points": "动态规划 / 双状态维护（最大与最小值应对负负得正）",
        "analysis_intuition": "与最大子数组和不同，乘法中存在“负负得正”。如果之前有一个很大的负数，再乘以一个负数就会变成极大的正数。因此如果只维护最大值，会丢失潜在的最优解。",
        "analysis_derivation": "我们必须同时维护当前位置的“最大乘积”和“最小乘积”（绝对值很大的负数）。每到一个位置，我们通过当前数、当前数乘上最大积、当前数乘上最小积这三者，分别更新当前位置的最大乘积和最小乘积，从而在 O(N) 时间和 O(1) 空间下得出全局最大乘积。",
        "code": """from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        cur_min = nums[0]
        cur_max = nums[0]
        for num in nums[1:]:
            temp = cur_max
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * temp, num * cur_min)
            res = max(res, cur_max)
        return res
"""
    },
    "07_find_minimum_in_rotated_sorted_array.py": {
        "title": "Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值)",
        "difficulty": "Medium",
        "key_points": "二分查找 (Binary Search)",
        "analysis_intuition": "在一个旋转过的升序数组中找最小值。直接遍历需要 O(N) 的时间。因为原本是有序的，我们需要在 O(log N) 的时间内解决。",
        "analysis_derivation": "使用二分查找。如果中间值 nums[mid] 大于右边界 nums[right]，说明旋转折返点在 mid 的右半边，最小值必定在 mid + 1 到 right 之间，因此 left = mid + 1。否则，说明右半边是单调递增的，最小值可能是 mid 本身或者在左半边，因此 right = mid。最终 left == right 即为最小值。",
        "code": """from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
"""
    },
    "08_search_in_rotated_sorted_array.py": {
        "title": "Search in Rotated Sorted Array (搜索旋转排序数组)",
        "difficulty": "Medium",
        "key_points": "二分查找 / 分段单调性判定",
        "analysis_intuition": "旋转数组中检索目标值。若直接遍历复杂度为 O(N)。我们需要利用二分查找达到 O(log N) 复杂度。",
        "analysis_derivation": "旋转数组有一个特性：如果从中间切开，两半中必然有一半是严格递增的。我们可以比较 nums[left] 和 nums[mid] 来确定哪一半是有序的：\n1. 如果左半部分有序，我们检查 target 是否在左半部分的单调区间内。如果在，我们收缩 right = mid - 1；否则去右半部分寻找（left = mid + 1）。\n2. 同理，如果右半部分有序，我们检查 target 是否在右半部单调区间内，收缩边界。如此这般折半查找。",
        "code": """from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
"""
    },
    "09_three_sum.py": {
        "title": "3Sum (三数之和)",
        "difficulty": "Medium",
        "key_points": "双指针 (Two Pointers) / 排序 (Sorting)",
        "analysis_intuition": "暴力搜索三个数，时间复杂度为 O(N^3)，且去重逻辑极其繁琐。如何进行优化并去重？",
        "analysis_derivation": "1. 首先对数组进行升序排序，这是使用双指针的前提。\n2. 固定第一个数 nums[i]，如果 nums[i] > 0 则后面不可能凑出 0，直接终止。如果 nums[i] == nums[i-1] 则跳过以去重。\n3. 在剩下的区间 [i+1, n-1] 中使用双指针 left 和 right 向中间夹逼。若三数之和小于 0 则 left += 1，大于 0 则 right -= 1。若等于 0，则记录答案，并移动双指针同时跳过重复的值去重。",
        "code": """from typing import List

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
"""
    },
    "10_container_with_most_water.py": {
        "title": "Container With Most Water (盛最多水的容器)",
        "difficulty": "Medium",
        "key_points": "双指针 (Two Pointers) / 贪心决策",
        "analysis_intuition": "暴力计算任意两块板组成的容器容量，复杂度为 O(N^2)。如何利用边界性质进行 O(N) 求解？",
        "analysis_derivation": "我们使用双指针 left 和 right 分别指向数组两端。容器的宽度是 right - left，高度取决于两板中的短板 min(height[left], height[right])。每次我们将短板那一侧的指针向内移动，因为如果移动长板那一侧，容器的宽度变小了，高度依然受限于保留下的短板，面积绝对不可能增大。因此，移动短板才是唯一有可能让面积增大的贪心策略。直到两指针相遇。",
        "code": """from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
"""
    }
}
