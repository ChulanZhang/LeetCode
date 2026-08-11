class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []

        def dfs(index):
            # All elements have been decided
            if index == len(nums):
                results.append(path.copy())
                return
            
            # Option 1: skip nums[index]
            dfs(index + 1)

            # Option 2: include nums[index]
            path.append(nums[index])
            dfs(index + 1)

            path.pop()

        dfs(0)
        return results


        # n = len(nums)
        # results = []

        # for i in range(2**n, 2**(n+1)):
        #     # 
        #     bitmask = bin(i)[3:]

        #     results.append([nums[j] for j in range(n) if bitmask[j] == "1"])

        # return results
        