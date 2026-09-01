class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Count the letters in every sticker once
        sticker_counts = [Counter(sticker) for sticker in stickers]

        @cache
        def dfs(remain: str) -> int:
            '''
            Return the minimum number of stickers needed
            to form the remaining characters
            '''
            # No letters left, so no more stickers are needed
            if remain == "":
                return 0
            
            # Count how many of each letter are still needed
            need = Counter(remain)
            min_stickers = float("inf")

            # remaining is sorted, so use its first letter as an anchor
            first_needed_char = remain[0]

            for sticker in sticker_counts:
                # This sticker cannot help remove the anchor letter
                if sticker[first_needed_char] == 0:
                    continue
                
                next_remaining = []
                # Subtract the letters provided by this sticker
                for char, required_count in need.items():
                    provided_count = sticker[char]
                    left_count = required_count - provided_count

                    if left_count > 0:
                        next_remaining.append(char * left_count)
                    
                next_remaining_str = "".join(sorted(next_remaining))

                next_result = dfs(next_remaining_str)

                if next_result != -1:
                    min_stickers = min(min_stickers, 1 + next_result)

            if min_stickers == float("inf"):
                return -1
            
            return min_stickers
        
        initial_remain = "".join(sorted(target))
        
        return dfs(initial_remain)

# TC: O(n x m x 2^m)
# SC: O(m x 2^m)