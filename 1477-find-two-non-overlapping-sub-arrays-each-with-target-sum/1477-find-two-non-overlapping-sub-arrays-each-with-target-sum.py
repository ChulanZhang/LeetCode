class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # sliding window + dp
        best = [float('inf')] * len(arr)
        ans = float('inf')
        prefix_sum = 0
        left = 0

        for right in range(len(arr)):
            prefix_sum += arr[right]
            
            # we want to find a subarray that has a sum of target
            # when prefix <= target, jump out of the while loop 
            while prefix_sum > target:
                prefix_sum -= arr[left]
                left += 1

            # when prefix_sum == target, we try to update the answer
            if prefix_sum == target:
                curr_len = right - left + 1

                # left > 0 means this cannot be the first subarray we found
                # best[left - 1] != float('inf') means we need an existing subarray that has a sum of target
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, best[left - 1] + curr_len)
                
                best[right] = curr_len
                
            if right > 0:
                best[right] = min(best[right], best[right - 1])

        return ans if ans != float('inf') else -1


        # prefix_to_index = {0: -1}
        # best = [float('inf')] * len(arr)
        # ans = float('inf')
        # prefix_sum = 0
        
        # for i, num in enumerate(arr):
        #     prefix_sum += num
        #     if prefix_sum - target in prefix_to_index:
        #         j = prefix_to_index[prefix_sum - target]
        #         curr_len = i - j

        #         if j >= 0 and best[j] != float('inf'):
        #             ans = min(ans, curr_len + best[j])

        #         best[i] = curr_len

        #     if i > 0:
        #         best[i] = min(best[i], best[i - 1])
            
        #     prefix_to_index[prefixsum] = i
        
        # if ans == float('inf'):
        #     return -1
        # else:
        #     return ans