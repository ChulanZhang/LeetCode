# Heap category data
PROBLEMS = {
    "74_top_k_frequent_elements.py": {
        "title": "Top K Frequent Elements (前 K 个高频元素)",
        "difficulty": "Medium",
        "key_points": "哈希计数表 + 桶排序 (Bucket Sort) O(N) 最优解 / 最小堆 (Min-Heap) O(N log K)",
        "analysis_intuition": "直觉：先用哈希表统计每个数字出现的频率，然后对频率排序，取前 k 大的数字。时间复杂度为 O(N log N)。或者，用一个大小为 k 的最小堆，维护当前最高频的 k 个元素，每次遇到新数字插入堆并调整，时间复杂度为 O(N log K)。",
        "analysis_derivation": "利用桶排序 (Bucket Sort) 实现 O(N) 极致优化破局：\n既然频数（Frequency）的取值范围被严格限定在 `[0, N]` 之间（N 为数组长度），我们完全可以使用**桶排序**的思想：\n1. 用哈希表统计每个数出现的频数。\n2. 创建一个大小为 `N + 1` 的列表 `buckets`。其中 `buckets[i]` 作为一个空列表，用来存放所有**出现频数刚好为 `i`** 的数字。\n3. 遍历哈希表，把数字放到它对应频数的桶 `buckets[frequency]` 中。\n4. **逆序收集**：从后往前（从最高频 `N` 到最低频 `0`）遍历 `buckets` 桶列表，依次将桶里的数搜集出来，直到我们搜集满 `k` 个元素为止。\n由于每个数字最多入桶出桶一次，且无需进行数值排序，总时间复杂度被降到了完美的 $O(N)$，空间复杂度也为 $O(N)$。这在面试中是优于堆排序的满分回答。",
        "code": """from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        \"\"\"
        时间复杂度: O(N) - 统计频数、入桶和搜集元素皆为 O(N)
        空间复杂度: O(N) - 存储频数哈希表与桶数组
        \"\"\"
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
"""
    },
    "75_find_median_from_data_stream.py": {
        "title": "Find Median from Data Stream (数据流的中位数)",
        "difficulty": "Hard",
        "key_points": "双堆平衡设计 (Dual Heaps) / 大顶堆与小顶堆",
        "analysis_intuition": "直觉：要把一个不断增加的数据流的中位数实时算出来，如果每次排序，插入复杂度是 O(N log N)，效率极低。如果用插入排序维护一个有序列表，每次插入是 O(N) 时间，仍然较慢。我们需要寻找能在 $O(\\log N)$ 时间内处理插入的方案。",
        "analysis_derivation": "大顶堆与小顶堆组合（双堆对对碰）破局：\n我们可以把所有数字拆分为**左右对称的两半部分**：\n- **左半部分**（较小的一半）：用一个**大顶堆 `small`** 存储。大顶堆的堆顶是这部分的最大值。\n- **右半部分**（较大的一半）：用一个**小顶堆 `large`** 存储。小顶堆的堆顶是这部分的最小值。\n这样，中位数就只与 `small` 的堆顶和 `large` 的堆顶有关。\n为了实现这个设计，在插入新元素 `num` 时：\n1. 默认先把 `num` 插入 `small`（左半部大顶堆）。为了将其负数化以实现大顶堆，我们压入 `-num`。\n2. 为了保证两堆的顺序，从 `small` 中弹出一个最大值，压入 `large` 中。\n3. **平衡两堆的大小**：我们约定左半部大顶堆 `small` 的元素个数最多比右半部小顶堆 `large`多 1 个，即：`len(small) >= len(large)`。如果刚才的交换导致 `len(large) > len(small)`，我们就从小顶堆 `large` 中弹出一个最小值，压入 `small` 中。\n4. **求中位数**：\n   - 如果 `len(small) > len(large)`，说明总个数为奇数，左侧多一个，中位数就是大顶堆 `small` 的堆顶。\n   - 如果两者长度相等，说明总个数为偶数，中位数就是 `(small 堆顶 + large 堆顶) / 2.0`。\n微调：每次插入和求中位数操作的复杂度均为 $O(\\log N)$，性能极高。",
        "code": """import heapq

class MedianFinder:
    def __init__(self):
        # small 是大顶堆，存较小的一半（Python heapq 默认为小顶堆，需将数值取反存储）
        self.small = []
        # large 是小顶堆，存较大的一半
        self.large = []

    def addNum(self, num: int) -> None:
        \"\"\"
        时间复杂度: O(log N) - 堆的压入与弹出操作
        \"\"\"
        # 1. 默认加入左半部大顶堆（压入负值）
        heapq.heappush(self.small, -num)
        
        # 2. 保证左半部的最大值小于或等于右半部的最小值：从左半部移出一个最大值到右半部
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)
        
        # 3. 维持大小平衡条件：len(small) >= len(large)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        \"\"\"
        时间复杂度: O(1) - 直接取堆顶元素
        \"\"\"
        if len(self.small) > len(self.large):
            # 奇数个，中位数在左半部最大值
            return float(-self.small[0])
            
        # 偶数个，取两堆顶的平均值
        return (-self.small[0] + self.large[0]) / 2.0
"""
    }
}
