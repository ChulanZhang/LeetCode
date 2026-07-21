class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 1
        curr_end = points[0][1]

        for x_start, x_end in points[1:]:
            if x_start > curr_end:
                arrows += 1
                curr_end = x_end
        
        return arrows
# dry run
# points = [[10,16],[2,8],[1,6],[7,12]]
# after sort
# points = [[1,6], [2,8], [7,12], [10,16]]
# x = 6
# x = 12
# time complexity: O(nlogN)