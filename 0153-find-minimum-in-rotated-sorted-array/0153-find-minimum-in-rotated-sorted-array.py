class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We maintain a search interval [left, right].
        #
        # IMPORTANT:
        # Both left and right are possible answers.
        # In other words, the minimum is always guaranteed
        # to be somewhere inside [left, right].
        left, right = 0, len(nums) - 1

        # We continue searching while there is more than
        # one candidate remaining.
        #
        # When left == right, only one candidate remains,
        # so that position must contain the minimum.
        while left < right:
            # Compute the middle index.
            #
            # This is equivalent to:
            # (left + right) // 2
            #
            # but this form avoids integer overflow
            # in languages such as C++ or Java.
            mid = left + (right - left) // 2

            # Compare nums[mid] with nums[right].
            #
            # Case 1:
            # nums[mid] > nums[right]
            #
            # Example:
            #
            # [4, 5, 6, 7, 0, 1, 2]
            #           ^
            #          mid
            #
            # nums[mid] = 7
            # nums[right] = 2
            #
            # This tells us that the rotation point
            # (and therefore the minimum) must be
            # strictly to the RIGHT of mid.
            #
            # mid itself cannot be the minimum,
            # so we can safely remove it from consideration.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Case 2:
            # nums[mid] < nums[right]
            #
            # This means the interval from mid to right
            # is normally sorted.
            #
            # Therefore, the minimum cannot be strictly
            # to the right of mid.
            #
            # However, nums[mid] itself COULD be the minimum,
            # so we must keep mid in the search interval.
            else:
                right = mid

        # The loop stops when:
        #
        # left == right
        #
        # At this point only one candidate remains,
        # and that position must contain the minimum.
        return nums[left]