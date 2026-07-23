class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for curr in intervals:
            if not merged or curr[0] > merged[-1][1]:
                merged.append(curr)
            else:
                merged[-1][1] = max(merged[-1][1], curr[1])
        return merged

# Time complexity: O(NlogN) for sorting
# Space complexity: O(N) for new array