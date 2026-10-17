class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        modify = 1
        for i in range(len(nums) - 1):
            # two choices: nums[i] = nums[i + 1] or nums[i + 1] = nums[i]
            if nums[i] > nums[i + 1]:
                if modify == 0:
                    return False
                modify = 0

                if i > 0 and nums[i - 1] > nums[i + 1]:
                    # to keep non-decreasing, increase nums[i + 1]
                    nums[i + 1] = nums[i]
                else:
                    # i == 0 or nums[i - 1] <= nums[i + 1]
                    nums[i] = nums[i + 1]
        return True
        