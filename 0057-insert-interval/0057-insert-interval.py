class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        results = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        results.append(newInterval)

        while i < n:
            results.append(intervals[i])
            i += 1
        
        return results
        