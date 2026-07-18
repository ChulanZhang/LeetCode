from typing import List, Optional, Dict, Set

# Top K Frequent Elements (前 K 个高频元素) - Medium
# 🔑 核心考点: 哈希计数表 + 桶排序 (Bucket Sort) O(N) 最优解 / 最小堆 (Min-Heap) O(N log K)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：先用哈希表统计每个数字出现的频率，然后对频率排序，取前 k 大的数字。时间复杂度为 O(N log N)。或者，用一个大小为 k 的最小堆，维护当前最高频的 k 个元素，每次遇到新数字插入堆并调整，时间复杂度为 O(N log K)。
#   - 思维推导: 
#     利用桶排序 (Bucket Sort) 实现 O(N) 极致优化破局：
#     既然频数（Frequency）的取值范围被严格限定在 `[0, N]` 之间（N 为数组长度），我们完全可以使用**桶排序**的思想：
#     1. 用哈希表统计每个数出现的频数。
#     2. 创建一个大小为 `N + 1` 的列表 `buckets`。其中 `buckets[i]` 作为一个空列表，用来存放所有**出现频数刚好为 `i`** 的数字。
#     3. 遍历哈希表，把数字放到它对应频数的桶 `buckets[frequency]` 中。
#     4. **逆序收集**：从后往前（从最高频 `N` 到最低频 `0`）遍历 `buckets` 桶列表，依次将桶里的数搜集出来，直到我们搜集满 `k` 个元素为止。
#     由于每个数字最多入桶出桶一次，且无需进行数值排序，总时间复杂度被降到了完美的 $O(N)$，空间复杂度也为 $O(N)$。这在面试中是优于堆排序的满分回答。

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        时间复杂度: O(N) - 统计频数、入桶和搜集元素皆为 O(N)
        空间复杂度: O(N) - 存储频数哈希表与桶数组
        """
        # 1. 统计各个数值出现的频数
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. 创建频数桶，索引 i 代表频数，buckets[i] 存所有频数为 i 的数
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # 3. 从后往前遍历桶（从最高频到最低频），搜集前 k 个元素
        res = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    
        return res

