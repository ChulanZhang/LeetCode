class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        for curr in intervals[1:]:
            if curr[0] > merged[-1][1]:
                merged.append(curr)
            else:
                merged[-1][1] = max(merged[-1][1], curr[1])
        return merged

# dry run
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# step 1: merged is empty so we init merged = [[1, 3]]
# step 2: curr[0] is 2, which is smaller than merged[-1][1] 3 so we need a merge. We take the larger number between the two intervals' right side. max(3, 6) = 6. merged = [[1, 6]]
# step 3: curr[0] is 8, which is large than merged[-1][1] (6) so we just add [8, 10] in the merged array
# step 4: curr[0] is 15, which is large than merged[-1][1] (10) so we add [15, 18]
# Time complexity: O(NlogN) for sorting
# Space complexity: O(N) for new array