from typing import List, Optional, Dict, Set

# Find Median from Data Stream (数据流的中位数) - Hard
# 🔑 核心考点: 双堆平衡设计 (Dual Heaps) / 大顶堆与小顶堆
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要把一个不断增加的数据流的中位数实时算出来，如果每次排序，插入复杂度是 O(N log N)，效率极低。如果用插入排序维护一个有序列表，每次插入是 O(N) 时间，仍然较慢。我们需要寻找能在 $O(\log N)$ 时间内处理插入的方案。
#   - 思维推导: 
#     大顶堆与小顶堆组合（双堆对对碰）破局：
#     我们可以把所有数字拆分为**左右对称的两半部分**：
#     - **左半部分**（较小的一半）：用一个**大顶堆 `small`** 存储。大顶堆的堆顶是这部分的最大值。
#     - **右半部分**（较大的一半）：用一个**小顶堆 `large`** 存储。小顶堆的堆顶是这部分的最小值。
#     这样，中位数就只与 `small` 的堆顶和 `large` 的堆顶有关。
#     为了实现这个设计，在插入新元素 `num` 时：
#     1. 默认先把 `num` 插入 `small`（左半部大顶堆）。为了将其负数化以实现大顶堆，我们压入 `-num`。
#     2. 为了保证两堆的顺序，从 `small` 中弹出一个最大值，压入 `large` 中。
#     3. **平衡两堆的大小**：我们约定左半部大顶堆 `small` 的元素个数最多比右半部小顶堆 `large`多 1 个，即：`len(small) >= len(large)`。如果刚才的交换导致 `len(large) > len(small)`，我们就从小顶堆 `large` 中弹出一个最小值，压入 `small` 中。
#     4. **求中位数**：
#        - 如果 `len(small) > len(large)`，说明总个数为奇数，左侧多一个，中位数就是大顶堆 `small` 的堆顶。
#        - 如果两者长度相等，说明总个数为偶数，中位数就是 `(small 堆顶 + large 堆顶) / 2.0`。
#     微调：每次插入和求中位数操作的复杂度均为 $O(\log N)$，性能极高。

import heapq

class MedianFinder:
    def __init__(self):
        # small 是大顶堆，存较小的一半（Python heapq 默认为小顶堆，需将数值取反存储）
        self.small = []
        # large 是小顶堆，存较大的一半
        self.large = []

    def addNum(self, num: int) -> None:
        """
        时间复杂度: O(log N) - 堆的压入与弹出操作
        """
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
        """
        时间复杂度: O(1) - 直接取堆顶元素
        """
        if len(self.small) > len(self.large):
            # 奇数个，中位数在左半部最大值
            return float(-self.small[0])
            
        # 偶数个，取两堆顶的平均值
        return (-self.small[0] + self.large[0]) / 2.0

