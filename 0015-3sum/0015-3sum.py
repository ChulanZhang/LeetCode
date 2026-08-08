class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array first.
        #
        # Sorting is important for two reasons:
        # 1. It allows us to use the two-pointer technique.
        # 2. Duplicate values become adjacent, making it easy
        #    to skip duplicate triplets.
        nums.sort()
        results = []
        n = len(nums)

        # nums[i] will be the FIRST number of the triplet.
        #
        # We only need to iterate until n - 2 because
        # we need at least two numbers after i:
        #
        # nums[i], nums[left], nums[right]
        for i in range(n - 2):
            # since the array is sorted, if nums[i] > 0, not possible to get sum of 0
            if nums[i] > 0:
                break
            # skip duplicated items
            # i > 0 is necessary because nums[i - 1]
            # should only be checked when a previous
            # element actually exists.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # left starts immediately after i.
            # right starts at the last element.
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # Case 1: total is too large.
                #
                # Moving right to the left gives us
                # a smaller number and decreases the total.
                if total > 0:
                    right -= 1
                # Case 2: total is too small.
                #
                # Because the array is sorted,
                # moving left to the right gives us
                # a larger number and increases the total.
                elif total < 0:
                    left += 1
                # Case 3: total == 0.
                #
                # We found a valid triplet.
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicated items
                    # Suppose we just used a 0.
                    #
                    # If the next nums[left] is also 0,
                    # using it would produce the same triplet.
                    #
                    # nums[left - 1] is the value we just used.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # nums[right + 1] is the value we just used
                    # before moving right one step left.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
        return results
        