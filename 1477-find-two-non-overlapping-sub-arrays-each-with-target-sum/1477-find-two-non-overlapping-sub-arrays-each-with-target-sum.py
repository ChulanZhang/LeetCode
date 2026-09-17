class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_to_index = {0: -1}
        best = [float('inf')] * len(arr)
        prefix = 0
        ans = float('inf')
        
        for i, num in enumerate(arr):
            prefix += num
            if prefix - target in prefix_to_index:
                j = prefix_to_index[prefix - target]
                curr_len = i - j

                if j >= 0 and best[j] != float('inf'):
                    ans = min(ans, curr_len + best[j])

                best[i] = curr_len

            if i > 0:
                best[i] = min(best[i], best[i - 1])
            
            prefix_to_index[prefix] = i
        
        if ans == float('inf'):
            return -1
        else:
            return ans
            



        # dic = {0: [1, -1, 0]}
        # count = 0
        # sub_array_len = []
        # s = 0
        # for idx, num in enumerate(arr):
        #     s += num
        #     dic[s] = [1, idx, 0]
        #     if s - target in dic and dic[s-target][2]==0:
        #         count += 1
        #         sub_array_len.append(idx- dic[s-target][1])
        #         dic[s-target][2] = 1
        #         dic[s][2] = 1
        
        # if count < 2:
        #     return -1
        # else:
        #     sub_array_len.sort()
        #     return sum(sub_array_len[:2])
        