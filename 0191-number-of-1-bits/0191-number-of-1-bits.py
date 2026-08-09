class Solution:
    def hammingWeight(self, n: int) -> int:
        results = 0
        while n:
            results += n & 1
            n >>= 1
        return results
        