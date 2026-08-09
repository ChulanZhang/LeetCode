class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []

        for num in range(n + 1):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            results.append(count)
        return results

        # dp = [0] * (n + 1)
        # for i in range(1, n+ 1):
        #     dp[i] = dp[i >> 1] + (i & 1)
        # return dp   