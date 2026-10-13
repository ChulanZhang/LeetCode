class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        results = 0
        d = {0: 1}
        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in d:
                results += d[prefix_sum - k]
            if prefix_sum in d:
                d[prefix_sum] += 1
            else:
                d[prefix_sum] = 1
        return results

        