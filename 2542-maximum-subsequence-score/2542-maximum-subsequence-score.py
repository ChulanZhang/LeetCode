class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # TC: O(nlogn)
        # SC: O(n)
         # Sort by nums2 descending, so current n2 is the minimum threshold
        pairs = sorted(zip(nums2, nums1), reverse = True)

        # Keep the largest k values from nums1
        min_heap = []
        current_sum = 0
        answer = 0

        for n2, n1 in pairs:
            heapq.heappush(min_heap, n1)
            current_sum += n1

            # Keep only the largest k nums1 values
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            # Current n2 acts as the minimum nums2
            if len(min_heap) == k:
                answer = max(answer, current_sum * n2)
        
        return answer
        