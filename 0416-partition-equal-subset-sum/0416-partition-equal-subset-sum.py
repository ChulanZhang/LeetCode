class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If total is odd, it cannot be split into
        # two subsets with equal sum.
        if total % 2 == 1:
            return False

        target = total // 2

        # dp[s] means:
        # using the numbers processed so far,
        # can we form a subset with sum exactly s?
        #
        # We only care about sums from 0 to target.
        dp = [False] * (target + 1)

        # Sum 0 is always possible:
        # choose no elements.
        dp[0] = True

        for num in nums:

            # Traverse backwards:
            # target -> ... -> num
            #
            # Why start from target?
            # We only care whether target can be formed.
            #
            # Why stop at num?
            # If s < num, we cannot use num to form s.
            #
            # Why backwards?
            # Each number can only be used once.
            # Going backwards ensures dp[s - num]
            # is still the state BEFORE using current num.
            for s in range(target, num - 1, -1):

                # Two ways to make sum s:
                #
                # 1. Do not use current num:
                #    dp[s] was already True.
                #
                # 2. Use current num:
                #    if we could previously make s - num,
                #    then adding num gives s.
                dp[s] = dp[s] or dp[s - num]

            # Optional optimization:
            # once target is reachable, answer is True.
            if dp[target]:
                return True

        return dp[target]
        