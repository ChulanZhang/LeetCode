class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


'''
        # We use a CLOSED search interval:
        #
        # [left, right]
        #
        # This means both left and right are valid indices
        # that may still contain the target.
        left = 0
        right = len(nums) - 1

        # Use <= instead of < because when left == right,
        # there is still ONE element left that has not
        # necessarily been checked.
        #
        # Example:
        #
        # left = 4
        # right = 4
        #
        # nums[4] may still be the target,
        # so we must enter the loop one more time.
        while left <= right:

            # Calculate the middle index.
            #
            # Equivalent to:
            #
            # mid = (left + right) // 2
            #
            # This form avoids integer overflow in languages
            # such as Java or C++.
            mid = left + (right - left) // 2

            # ------------------------------------------------
            # Step 1:
            # Always check mid first.
            #
            # If nums[mid] is the target, return immediately.
            # ------------------------------------------------
            if nums[mid] == target:
                return mid

            # ------------------------------------------------
            # Step 2:
            # Determine which half is sorted.
            #
            # If nums[left] <= nums[mid],
            # then the LEFT half [left, mid] is sorted.
            #
            # Example:
            #
            # [4, 5, 6, 7, 0, 1, 2]
            #  L        M        R
            #
            # nums[left] = 4
            # nums[mid]  = 7
            #
            # 4 <= 7
            #
            # Therefore [4, 5, 6, 7] is sorted.
            # ------------------------------------------------
            if nums[left] <= nums[mid]:

                # ------------------------------------------------
                # Now that the left half is sorted,
                # check whether target lies inside it.
                #
                # The range is:
                #
                # nums[left] <= target < nums[mid]
                #
                # Why include nums[left]?
                # Because nums[left] itself may be the target.
                #
                # Why NOT include nums[mid]?
                # Because nums[mid] == target was already
                # checked above.
                # ------------------------------------------------
                if nums[left] <= target < nums[mid]:

                    # Target must be in the left half.
                    #
                    # We already know nums[mid] != target,
                    # so mid itself can be safely removed.
                    #
                    # New search interval:
                    #
                    # [left, mid - 1]
                    right = mid - 1

                else:
                    # Target is NOT inside the sorted left half,
                    # so it must be in the other half
                    # if it exists at all.
                    #
                    # Again, nums[mid] != target,
                    # so we can exclude mid.
                    #
                    # New search interval:
                    #
                    # [mid + 1, right]
                    left = mid + 1

            # ------------------------------------------------
            # If the left half is NOT sorted,
            # then the RIGHT half must be sorted.
            #
            # Example:
            #
            # [6, 7, 0, 1, 2, 4, 5]
            #  L        M        R
            #
            # nums[left] > nums[mid]
            #
            # So the rotation point is somewhere
            # in the left half, which means
            # [mid, right] must be sorted.
            # ------------------------------------------------
            else:

                # Check whether target lies inside
                # the sorted right half.
                #
                # Range:
                #
                # nums[mid] < target <= nums[right]
                #
                # nums[mid] is excluded because
                # it was already checked.
                #
                # nums[right] is included because
                # nums[right] may still be the target.
                if nums[mid] < target <= nums[right]:

                    # Target must be on the right.
                    #
                    # nums[mid] is already known not to be target,
                    # so safely exclude it.
                    left = mid + 1

                else:
                    # Target is not inside the sorted right half,
                    # so search the left side.
                    right = mid - 1

        # The loop ends when:
        #
        # left > right
        #
        # which means the search interval is empty.
        # Therefore target does not exist in nums.
        return -1
'''
        