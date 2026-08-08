class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers: left, right
        # area = min(height[left], height[right]) * (right - left)
        left, right = 0, len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            curr_height = min(height[left], height[right]) 
            max_water = max(max_water, width * curr_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


        