class Solution:
    def countBits(self, n: int) -> List[int]:
        # For loop solution, based on Leetcode 191
        # TC: O(nlogn)
        # SC: O(1)
        # ans = []
        # for i in range(n + 1):
        #     count = 0
        #     while i:
        #         # i & 1 will keep i's last bit
        #         count += i & 1
        #         # move i to the right by 1 bit, same as divided by 2
        #         i >>= 1
        #     ans.append(count)
        # return ans

        # DP solution: we can reuse the results from smaller numbers
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp

