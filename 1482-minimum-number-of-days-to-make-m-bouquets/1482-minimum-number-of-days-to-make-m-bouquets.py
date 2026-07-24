class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def can_make(day: int) -> bool:
            bouquets = 0
            consecutive = 0

            for bloom in bloomDay:
                if bloom <= day:
                    consecutive += 1
                
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0

                        if bouquets == m:
                            return True
                else:
                    # non-bloom day will break consecutive
                    consecutive = 0
            return False
        
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        