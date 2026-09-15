class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = sorted(i[0] for i in intervals)
        end_time = sorted(i[1] for i in intervals)

        min_rooms = 1
        start_pointer, end_pointer = 1, 0

        while start_pointer < len(intervals):
            if start_time[start_pointer] < end_time[end_pointer]:
                min_rooms += 1
            else:
                end_pointer += 1
            
            start_pointer += 1
        return min_rooms
# TC: O(nlogn) for sorting
# SC: O(n) for start_time and end_time