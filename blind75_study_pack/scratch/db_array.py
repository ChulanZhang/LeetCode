# Array category data
PROBLEMS = {
    "01_two_sum.py": {
        "title": "Two Sum",
        "difficulty": "Easy",
        "key_points": "Hash Map - Space-Time Tradeoff",
        "analysis_intuition": "The naive approach is using nested loops to check every pair of elements for a sum equal to the target, which costs O(N^2) time complexity. This is inefficient for large inputs. We need to avoid using the same element twice and handle duplicate values correctly.",
        "analysis_derivation": "To optimize the time complexity to O(N), we can trade space for time. By traversing the array once and storing each visited element and its index in a hash map, we can check if the complement (target - current_value) exists in the hash map in O(1) average time. If it does, we return their indices.",
        "code": """from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store value-to-index mapping
        num_to_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            # Check if the complement already exists in the map
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            # Store the current number with its index
            num_to_idx[num] = i
        return []
"""
    },
    "02_best_time_to_buy_and_sell_stock.py": {
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "key_points": "Greedy / Dynamic Programming - Single Pass",
        "analysis_intuition": "The brute-force solution calculates the profit for every possible buy-and-sell pair (where sell day > buy day) using nested loops, which takes O(N^2) time complexity.",
        "analysis_derivation": "Since you must buy before you can sell, we can solve this in a single pass. While traversing the prices, we maintain two variables: the minimum price seen so far (`min_price`) and the maximum profit achieved (`max_profit`). For each price, we update `min_price` and calculate the potential profit if we sold on that day (`price - min_price`), updating `max_profit` if this potential profit is larger.",
        "code": """from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = float('inf')  # Track the minimum price seen so far
        max_profit = 0            # Track the maximum profit seen so far
        for price in prices:
            if price < min_price:
                min_price = price  # Update min price if a lower buying price is found
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max profit if selling today yields more
        return max_profit
"""
    },
    "03_contains_duplicate.py": {
        "title": "Contains Duplicate",
        "difficulty": "Easy",
        "key_points": "Hash Set - Early Return Optimization",
        "analysis_intuition": "A brute-force solution compares every pair of elements, resulting in O(N^2) time complexity. Using `len(set(nums)) != len(nums)` is clean but does not allow early return, which might waste memory and computation on large arrays when a duplicate is found early.",
        "analysis_derivation": "To achieve O(N) time complexity, we can use a hash set to keep track of visited numbers. As we iterate through the array, we check if the current number is already in the set. If it is, we return True immediately (early return). Otherwise, we add it to the set. If the loop completes, it means all elements are unique.",
        "code": """from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()  # Set to track unique visited numbers
        for num in nums:
            # If the number is already visited, we found a duplicate
            if num in visited:
                return True
            visited.add(num)  # Add current number to visited set
        return False
"""
    },
    "04_product_of_array_except_self.py": {
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "key_points": "Prefix & Suffix Products - Space Optimization",
        "analysis_intuition": "The simplest method is to calculate the product of all elements and then divide it by each `nums[i]`. However, division is prohibited, and division by zero errors will occur if the array contains zero.",
        "analysis_derivation": "The product of all elements except `nums[i]` can be decomposed into: the product of all elements to the left of `i` (prefix product) multiplied by the product of all elements to the right of `i` (suffix product). We can store the prefix products directly in the output array. Then, scanning backwards, we maintain a running suffix product in a variable and multiply it into the output array at each index. This achieves O(1) auxiliary space.",
        "code": """from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Calculate prefix products and store them in the answer array
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
            
        # Calculate suffix products on the fly and multiply them into answer
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]
            
        return answer
"""
    },
    "05_maximum_subarray.py": {
        "title": "Maximum Subarray",
        "difficulty": "Medium",
        "key_points": "Dynamic Programming (Kadane's Algorithm)",
        "analysis_intuition": "Brute-force checks all subarray starting and ending positions, which takes O(N^2) time complexity. If the array contains only negative numbers, initializing the maximum subarray sum to 0 is a common mistake; it must be initialized to the first element or negative infinity.",
        "analysis_derivation": "At each position in the array, we decide whether to add the current number to the existing subarray sum, or to start a new subarray from the current number. If the previous cumulative sum is negative, it will only decrease the sum of any subsequent subarray, so we discard it and start fresh. The state transition is: `current_sum = max(num, current_sum + num)`. We track the maximum value seen during this process.",
        "code": """from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]  # Max subarray sum ending at current index
        max_sum = nums[0]      # Global max subarray sum
        
        for num in nums[1:]:
            # Choose to extend the previous subarray or start a new one
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum
"""
    },
    "06_maximum_product_subarray.py": {
        "title": "Maximum Product Subarray",
        "difficulty": "Medium",
        "key_points": "Dynamic Programming - Double State Tracking",
        "analysis_intuition": "Unlike the subarray sum problem, multiplication supports 'two negatives make a positive'. A very small negative number can become a large positive number when multiplied by another negative. Thus, tracking only the maximum product is insufficient.",
        "analysis_derivation": "We must maintain both the current maximum product and the current minimum product (which could be a large negative number). For each element, we calculate the potential new max and min by comparing the current number, current number * prev_max, and current number * prev_min. This allows us to handle sign flips in O(N) time and O(1) space.",
        "code": """from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        cur_min = nums[0]  # Minimum product seen ending at current index
        cur_max = nums[0]  # Maximum product seen ending at current index
        
        for num in nums[1:]:
            temp = cur_max
            # Update current max and min considering possible sign changes
            cur_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * temp, num * cur_min)
            res = max(res, cur_max)
            
        return res
"""
    },
    "07_find_minimum_in_rotated_sorted_array.py": {
        "title": "Find Minimum in Rotated Sorted Array",
        "difficulty": "Medium",
        "key_points": "Binary Search",
        "analysis_intuition": "Finding the minimum in a rotated sorted array. A linear scan takes O(N). Because the array was originally sorted, we must solve it in O(log N) time using binary search.",
        "analysis_derivation": "Using binary search, if the middle value `nums[mid]` is greater than the right boundary `nums[right]`, it means the rotation inflection point lies to the right of `mid`, so the minimum must be in the range `[mid + 1, right]`. Otherwise, the right half is sorted, and the minimum is either `nums[mid]` or lies to the left of `mid`. Thus, we update `right = mid`. We repeat this until `left == right`.",
        "code": """from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Inflection point must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            # Inflection point is at mid or to the left of mid
            else:
                right = mid
        return nums[left]
"""
    },
    "08_search_in_rotated_sorted_array.py": {
        "title": "Search in Rotated Sorted Array",
        "difficulty": "Medium",
        "key_points": "Binary Search - Split Monotonicity",
        "analysis_intuition": "Searching for a target in a rotated sorted array. A linear scan takes O(N). We need to leverage binary search to achieve O(log N) complexity.",
        "analysis_derivation": "A rotated sorted array has a key property: if split in half, at least one half is always strictly sorted. We can compare `nums[left]` and `nums[mid]` to determine which half is sorted:\n1. If the left half is sorted, we check if the target lies within the range of this sorted half. If so, we search left (`right = mid - 1`), else we search right (`left = mid + 1`).\n2. If the right half is sorted, we check if the target lies within the range of this sorted half, adjusting the binary search bounds accordingly.",
        "code": """from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is inside the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half must be sorted
            else:
                # Check if target is inside the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
"""
    },
    "09_three_sum.py": {
        "title": "3Sum",
        "difficulty": "Medium",
        "key_points": "Two Pointers - Sorting",
        "analysis_intuition": "A brute-force search of three numbers takes O(N^3) time complexity and has extremely tedious duplicate removal logic. We need an efficient way to sort, prune, and skip duplicate elements.",
        "analysis_derivation": "1. First, sort the array in ascending order to use two pointers.\n2. Fix the first number `nums[i]`. If `nums[i] > 0`, it's impossible to sum to 0 with subsequent positive numbers, so we break. If `nums[i] == nums[i-1]`, skip it to avoid duplicate triplets.\n3. For the remaining range `[i + 1, n - 1]`, use two pointers `left` and `right`. If the sum is less than 0, increment `left`; if greater than 0, decrement `right`. If equal to 0, record the triplet, and shift both pointers while skipping duplicate values to prevent duplicates.",
        "code": """from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort first to enable two pointers
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break  # Pivot cannot be positive
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate pivots
                
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # Shift left and right pointers while skipping duplicates
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
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "key_points": "Two Pointers - Greedy Pointer Shifting",
        "analysis_intuition": "Calculating the volume for every possible pair of lines takes O(N^2) time complexity. We can leverage the boundaries and solve this in O(N) using two pointers.",
        "analysis_derivation": "We place two pointers at the two ends of the array. The width of the container is `right - left`, and the height is bounded by the shorter line `min(height[left], height[right])`. Each time, we shift the pointer pointing to the shorter line inward. Shifting the pointer pointing to the longer line cannot increase the area because the height is still capped by the shorter line, while the width decreases. Thus, moving the shorter line is the only greedy strategy that could potentially yield a larger area.",
        "code": """from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)
            # Greedily move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
"""
    }
}
