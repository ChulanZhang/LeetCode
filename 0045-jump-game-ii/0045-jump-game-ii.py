class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = 0
        jumps = 0
        
        # 只要右边界还没覆盖到终点下标
        while r < n - 1:
            farthest = 0
            # 扫描当前跳跃窗口 [l, r] 内能到达的最远位置
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # 推进到下一跳的覆盖区间
            l = r + 1
            r = farthest
            jumps += 1
            
        return jumps
        # i = 0
        # jumps = 0
        # while i < len(nums) -1:
        #     max_location = i + nums[i]
        #     idx = i
        #     for j in range(i,i+nums[i]+1):
        #         if j < len(nums) and (j + nums[j]) >= max_location:
        #             max_location = nums[j] + j
        #             idx = j
        #     i = idx
        #     print(i)
        #     jumps += 1
        #     print(jumps) 
	
        # return jumps

        