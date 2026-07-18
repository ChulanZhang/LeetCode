# 30天算法冲刺通关计划 (MLSys PhD 专属定制)

> **冲刺教练寄语**：专为 MLSys 背景定制，在打牢双指针、二分、递归、树、图等算法底子的同时，深度融合系统级缓存（LRU/LFU）、环形队列、并发安全、位运算量化等底层机制，消除代码手生感。

## 30天全景规划看板

| 阶段 | 日期 | 核心主题 | 每日题量 |
|---|---|---|---|
| Phase 1 | Day 01 | 数组与双指针 (Array & Two Pointers) | 3 题 |
| Phase 1 | Day 02 | 滑动窗口 (Sliding Window) | 3 题 |
| Phase 1 | Day 03 | 快慢指针与循环检测 (Fast & Slow Pointers) | 3 题 |
| Phase 1 | Day 04 | 单调栈与边界判定 (Monotonic Stack) | 3 题 |
| Phase 1 | Day 05 | 单调队列与滑动指标 (Monotonic Queue) | 2 题 |
| Phase 1 | Day 06 | 前缀和与差分数组 (Prefix Sums & Difference Arrays) | 3 题 |
| Phase 1 | Day 07 | 矩阵变换与缓存局部性 (Matrix Operations & Locality) | 3 题 |
| Phase 2 | Day 08 | 二分查找与折半搜索 (Binary Search) | 3 题 |
| Phase 2 | Day 09 | 二分查找进阶与实数域 (Advanced Binary Search) | 3 题 |
| Phase 2 | Day 10 | 二叉树递归与层序遍历 (Tree Recursion & BFS) | 3 题 |
| Phase 2 | Day 11 | 二叉搜索树与最近公共祖先 (BST & LCA) | 3 题 |
| Phase 2 | Day 12 | 二叉树构造与路径累加 (Tree Construction & DFS) | 3 题 |
| Phase 2 | Day 13 | 回溯与决策搜索空间 (Backtracking basics) | 3 题 |
| Phase 2 | Day 14 | 高阶回溯与搜索空间剪枝 (Advanced Backtracking) | 2 题 |
| Phase 3 | Day 15 | 图的遍历与拓扑连通 (Graph Traversals) | 3 题 |
| Phase 3 | Day 16 | 拓扑排序与计算依赖调度 (Topological Sort) | 3 题 |
| Phase 3 | Day 17 | 并查集与等价类连通 (Union Find) | 3 题 |
| Phase 3 | Day 18 | 前缀树与高性能词典 (Trie) | 3 题 |
| Phase 3 | Day 19 | 堆与优先队列调度 (Heaps & Schedulers) | 3 题 |
| Phase 3 | Day 20 | 位运算与低精度表示 (Bit Manipulation & Quantization) | 4 题 |
| Phase 3 | Day 21 | 缓存算法手撕实战 (Cache System Implementation) | 3 题 |
| Phase 4 | Day 22 | 一维动态规划与拆分决策 (1D DP) | 3 题 |
| Phase 4 | Day 23 | 子序列与背包模型 (Sequence & Knapsack DP) | 3 题 |
| Phase 4 | Day 24 | 二维动态规划与网格状态 (2D DP) | 3 题 |
| Phase 4 | Day 25 | 区间与树形动态规划 (Interval & Tree DP) | 3 题 |
| Phase 4 | Day 26 | 贪心决策与区间调度 (Greedy Algorithms) | 3 题 |
| Phase 4 | Day 27 | 区间重叠与多维度调度 (Intervals & Scheduling) | 3 题 |
| Phase 4 | Day 28 | 全真高压模拟 Day 1 (Google/Meta 偏底层高频真题) | 2 题 |
| Phase 4 | Day 29 | 全真高压模拟 Day 2 (NVIDIA/Apple 硬件与并发关联真题) | 2 题 |
| Phase 4 | Day 30 | 全真高压模拟 Day 3 (大厂 Hard 极客挑战终局模拟) | 3 题 |

---

## Phase 1: 基础与指针直觉 (Day 1-7)
**阶段目标**：掌握左右双指针、快慢指针、滑动窗口、单调栈等核心模板，建立数组与链表肌肉记忆，戒掉低级指针越界Bug。

### 📅 Day 01 - 数组与双指针 (Array & Two Pointers)

- **LeetCode 1**: [Two Sum](https://leetcode.com/problems/two-sum/) | **[Easy]**
  - 🔑 **考点**: 哈希表 / 双指针
  - 💻 **本地复盘模板**: [sprint_plan/templates/day01_q001_two_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day01_q001_two_sum.py)
  - 🧠 **MLSys 底层映射**: 在系统底层或 GPU 算子设计中，利用静态哈希映射或有序双指针进行匹配是快速查表的最基本手段。时间复杂度从 O(N^2) 降至 O(N)，属于空间换时间的典范。

- **LeetCode 15**: [3Sum](https://leetcode.com/problems/3sum/) | **[Medium]**
  - 🔑 **考点**: 排序 + 双指针左右逼近
  - 💻 **本地复盘模板**: [sprint_plan/templates/day01_q015_3sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day01_q015_3sum.py)
  - 🧠 **MLSys 底层映射**: 左右双指针的核心是利用单调性进行状态缩减。通过排序，使得我们可以利用单调性移动两端指针，避免暴力三层循环。

- **LeetCode 11**: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | **[Medium]**
  - 🔑 **考点**: 双指针 + 贪心移动短板
  - 💻 **本地复盘模板**: [sprint_plan/templates/day01_q011_container_with_most_water.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day01_q011_container_with_most_water.py)
  - 🧠 **MLSys 底层映射**: 贪心策略在分布式系统的调度决策（例如最少网络开销节点选择）中极为常见。移动高度低的一侧是唯一能让后续面积增大的可能。

---
### 📅 Day 02 - 滑动窗口 (Sliding Window)

- **LeetCode 3**: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | **[Medium]**
  - 🔑 **考点**: 双指针滑动窗口 + 哈希集合
  - 💻 **本地复盘模板**: [sprint_plan/templates/day02_q003_longest_substring_without_repeating_characters.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day02_q003_longest_substring_without_repeating_characters.py)
  - 🧠 **MLSys 底层映射**: 滑动窗口用于处理连续子区间问题。在网络协议层（例如 TCP 滑动窗口接收缓冲区管理）和流处理系统（比如计算过去 10s 的平均推理请求率）中，这是基本的操作模式。

- **LeetCode 424**: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | **[Medium]**
  - 🔑 **考点**: 滑动窗口 + 局部频数统计优化
  - 💻 **本地复盘模板**: [sprint_plan/templates/day02_q424_longest_repeating_character_replacement.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day02_q424_longest_repeating_character_replacement.py)
  - 🧠 **MLSys 底层映射**: 窗口大小 L 减去出现最多的字符频数 max_freq 必须小于等于 k。通过维护历史最大频数 max_freq 避免了在窗口收缩时重新统计频数的 O(26) 扫描。

- **LeetCode 76**: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | **[Hard]**
  - 🔑 **考点**: 双哈希表计数 + 最优窗口收缩
  - 💻 **本地复盘模板**: [sprint_plan/templates/day02_q076_minimum_window_substring.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day02_q076_minimum_window_substring.py)
  - 🧠 **MLSys 底层映射**: Hard 级别的滑动窗口标杆。在编译器词法分析（Lexical Analysis）和编译器底层字符串匹配扫描器中，此类逻辑经常被用来作为高性能语法解析的核心组件。

---
### 📅 Day 03 - 快慢指针与循环检测 (Fast & Slow Pointers)

- **LeetCode 141**: [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | **[Easy]**
  - 🔑 **考点**: 快慢指针 (Floyd 判圈算法)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day03_q141_linked_list_cycle.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day03_q141_linked_list_cycle.py)
  - 🧠 **MLSys 底层映射**: 快慢指针在内存管理器中用来判断数据块链表（比如堆内存块分配链表）是否因越界或 Bug 发生了指针环形闭合，是基础防爆内存工具。

- **LeetCode 142**: [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | **[Medium]**
  - 🔑 **考点**: 快慢指针寻找环起点
  - 💻 **本地复盘模板**: [sprint_plan/templates/day03_q142_linked_list_cycle_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day03_q142_linked_list_cycle_ii.py)
  - 🧠 **MLSys 底层映射**: 数学推导：从头节点到环起点的距离等于快慢指针相遇点到环起点的距离。本题展示了指针距离计算的绝对控制能力。

- **LeetCode 202**: [Happy Number](https://leetcode.com/problems/happy-number/) | **[Easy]**
  - 🔑 **考点**: 隐式链表判圈
  - 💻 **本地复盘模板**: [sprint_plan/templates/day03_q202_happy_number.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day03_q202_happy_number.py)
  - 🧠 **MLSys 底层映射**: 数字变换过程可抽象为隐式有向图中的单链表。当变换陷入死循环时，即可使用快慢指针检测，无需借助哈希表，实现 O(1) 空间占用。

---
### 📅 Day 04 - 单调栈与边界判定 (Monotonic Stack)

- **LeetCode 496**: [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | **[Easy]**
  - 🔑 **考点**: 单调递减栈
  - 💻 **本地复盘模板**: [sprint_plan/templates/day04_q496_next_greater_element_i.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day04_q496_next_greater_element_i.py)
  - 🧠 **MLSys 底层映射**: 单调栈是解决 '寻找下一个更大元素' 问题的利器。通过栈的单调性，我们可以保证每个元素仅入栈出栈一次，实现时间复杂度 O(N)。

- **LeetCode 739**: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | **[Medium]**
  - 🔑 **考点**: 单调递减栈保存索引
  - 💻 **本地复盘模板**: [sprint_plan/templates/day04_q739_daily_temperatures.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day04_q739_daily_temperatures.py)
  - 🧠 **MLSys 底层映射**: 在时间轴分析与系统性能指标监控（如计算延迟首次下降的天数）中，基于单调栈的后向距离计算是经典的流处理计算节点结构。

- **LeetCode 84**: [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | **[Hard]**
  - 🔑 **考点**: 单调递增栈 + 哨兵节点
  - 💻 **本地复盘模板**: [sprint_plan/templates/day04_q084_largest_rectangle_in_histogram.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day04_q084_largest_rectangle_in_histogram.py)
  - 🧠 **MLSys 底层映射**: 系统内存碎片的合并计算（如寻址连续物理页面的最大矩阵）中，此算法提供了 O(N) 的极速求解器。对栈顶弹出的高板计算面积是核心。

---
### 📅 Day 05 - 单调队列与滑动指标 (Monotonic Queue)

- **LeetCode 239**: [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | **[Hard]**
  - 🔑 **考点**: 单调队列 (双端队列 deque)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day05_q239_sliding_window_maximum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day05_q239_sliding_window_maximum.py)
  - 🧠 **MLSys 底层映射**: 在 MLSys 的推理服务器中，我们需要计算滑动时间窗口内的最大推理耗时或吞吐量。基于双端队列的单调队列算法，保证每个元素入队出队最多一次，实现了完美的 O(N) 实时监控统计。

- **LeetCode 862**: [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | **[Hard]**
  - 🔑 **考点**: 前缀和 + 单调双端队列
  - 💻 **本地复盘模板**: [sprint_plan/templates/day05_q862_shortest_subarray_with_sum_at_least_k.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day05_q862_shortest_subarray_with_sum_at_least_k.py)
  - 🧠 **MLSys 底层映射**: 在包含负值的数据流中寻找满足累加阈值的最短子区间。利用前缀和与单调递增队列，可在 O(N) 时间内完成最优区间检索。

---
### 📅 Day 06 - 前缀和与差分数组 (Prefix Sums & Difference Arrays)

- **LeetCode 304**: [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d---immutable/) | **[Medium]**
  - 🔑 **考点**: 二维前缀和积分图
  - 💻 **本地复盘模板**: [sprint_plan/templates/day06_q304_range_sum_query_2d___immutable.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day06_q304_range_sum_query_2d___immutable.py)
  - 🧠 **MLSys 底层映射**: 二维前缀和本质上是计算机视觉和图像处理中的“积分图 (Integral Image)”。在 CNN（卷积神经网络）的池化层或局部求和加速中，利用前缀和可以将任何局部区间求和的复杂度从 O(H*W) 直接降至 O(1)。

- **LeetCode 1109**: [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) | **[Medium]**
  - 🔑 **考点**: 一维差分数组
  - 💻 **本地复盘模板**: [sprint_plan/templates/day06_q1109_corporate_flight_bookings.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day06_q1109_corporate_flight_bookings.py)
  - 🧠 **MLSys 底层映射**: 差分数组用于高效处理“区间批量加减运算”。在系统调度中，如果要在某个时间区间内给所有任务分配相同的算力资源，使用差分数组可实现 O(1) 的记录，并在最后通过一次前缀和扫描还原，复杂度为 O(N)。

- **LeetCode 1094**: [Car Pooling](https://leetcode.com/problems/car-pooling/) | **[Medium]**
  - 🔑 **考点**: 差分数组检验超载边界
  - 💻 **本地复盘模板**: [sprint_plan/templates/day06_q1094_car_pooling.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day06_q1094_car_pooling.py)
  - 🧠 **MLSys 底层映射**: 在分布式系统的并发容量限制（或 GPU 显存分配动态阈值）检测中，将区间分配需求转换为差分数组来一曲校验最大并发数是否超标，是极佳的调度前置步骤。

---
### 📅 Day 07 - 矩阵变换与缓存局部性 (Matrix Operations & Locality)

- **LeetCode 48**: [Rotate Image](https://leetcode.com/problems/rotate-image/) | **[Medium]**
  - 🔑 **考点**: 矩阵原地转置 + 水平翻转
  - 💻 **本地复盘模板**: [sprint_plan/templates/day07_q048_rotate_image.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day07_q048_rotate_image.py)
  - 🧠 **MLSys 底层映射**: 转置和反转的操作完全符合计算机系统结构中“缓存局部性 (Cache Locality)”的考察。在 MLSys 底层中，Tensor 维度的置换（Transpose/Permute）是高频算子，如何实现一维连续内存的高速 stride 寻址和原地调换是 GPU 算子优化的核心。

- **LeetCode 54**: [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | **[Medium]**
  - 🔑 **考点**: 边界指针收缩模拟
  - 💻 **本地复盘模板**: [sprint_plan/templates/day07_q054_spiral_matrix.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day07_q054_spiral_matrix.py)
  - 🧠 **MLSys 底层映射**: 模拟螺旋轨迹访问。对边界条件（上、下、左、右）进行严格的动态收缩，考察了面试中对大矩阵边界控制无 Bug 编写的基本功。

- **LeetCode 73**: [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | **[Medium]**
  - 🔑 **考点**: 首行首列作为状态标记器
  - 💻 **本地复盘模板**: [sprint_plan/templates/day07_q073_set_matrix_zeroes.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day07_q073_set_matrix_zeroes.py)
  - 🧠 **MLSys 底层映射**: 内存极度受限时的空间优化方案。通过把中间元素的置零标记投影到矩阵第一行和第一列，实现了 O(1) 的额外空间复杂度。在嵌入式或边缘设备算子中极为实用。

---
## Phase 2: 树与二分查找 (Day 8-14)
**阶段目标**：突破二分查找边界控制（防死循环），精通二叉树与 BST 性质的递归推导，克服递归恐惧。

### 📅 Day 08 - 二分查找与折半搜索 (Binary Search)

- **LeetCode 704**: [Binary Search](https://leetcode.com/problems/binary-search/) | **[Easy]**
  - 🔑 **考点**: 标准二分查找模板
  - 💻 **本地复盘模板**: [sprint_plan/templates/day08_q704_binary_search.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day08_q704_binary_search.py)
  - 🧠 **MLSys 底层映射**: 二分查找的精髓在于边界区间的划分与防死循环条件。在底层系统设计中，诸如内存页表快速检索、有序键值对存储的检索，二分查找是必不可少的 O(log N) 算法。

- **LeetCode 33**: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | **[Medium]**
  - 🔑 **考点**: 分段单调性二分查找
  - 💻 **本地复盘模板**: [sprint_plan/templates/day08_q033_search_in_rotated_sorted_array.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day08_q033_search_in_rotated_sorted_array.py)
  - 🧠 **MLSys 底层映射**: 经典的旋转数组检索。核心破局点是：如果从中间剖开，旋转有序数组的左右两半必然有一半是严格升序的。通过判断哪半边有序，可以照样将搜索范围折半。

- **LeetCode 153**: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | **[Medium]**
  - 🔑 **考点**: 二分收缩旋转点
  - 💻 **本地复盘模板**: [sprint_plan/templates/day08_q153_find_minimum_in_rotated_sorted_array.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day08_q153_find_minimum_in_rotated_sorted_array.py)
  - 🧠 **MLSys 底层映射**: 与右边界 nums[right] 对比。如果 nums[mid] > nums[right] 说明最小值在右侧；否则在左侧。考察了在非经典升序数组中发掘单调性进行二分收缩的能力。

---
### 📅 Day 09 - 二分查找进阶与实数域 (Advanced Binary Search)

- **LeetCode 74**: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | **[Medium]**
  - 🔑 **考点**: 二维矩阵一维化二分
  - 💻 **本地复盘模板**: [sprint_plan/templates/day09_q074_search_a_2d_matrix.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day09_q074_search_a_2d_matrix.py)
  - 🧠 **MLSys 底层映射**: 行优先存储（Row-major order）的二维矩阵在内存中是一维连续存储的。通过逻辑上的映射 `(row, col) = (mid // n, mid % n)`，可以直接在连续内存上跑标准二分，避免昂贵的行转换开销。

- **LeetCode 162**: [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | **[Medium]**
  - 🔑 **考点**: 寻找局部峰值 / 爬坡法
  - 💻 **本地复盘模板**: [sprint_plan/templates/day09_q162_find_peak_element.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day09_q162_find_peak_element.py)
  - 🧠 **MLSys 底层映射**: 在机器学习的最优化理论和系统的自适应参数调节中，“爬坡法（Hill Climbing）”是搜索局部最优的基本手段。只要当前位置处于上升趋势，则峰值必然在右侧，从而实现 O(log N) 局部峰值定位。

- **LeetCode 4**: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | **[Hard]**
  - 🔑 **考点**: 双数组划分 + 对角二分
  - 💻 **本地复盘模板**: [sprint_plan/templates/day09_q004_median_of_two_sorted_arrays.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day09_q004_median_of_two_sorted_arrays.py)
  - 🧠 **MLSys 底层映射**: 在分布式数据库或多机多卡 Tensor 拆分中，经常需要对两个异构且分别有序的数据块进行合并定位中位数。利用二分较小数组划分线的方法，可在 O(log(min(M, N))) 时间内精确分割。

---
### 📅 Day 10 - 二叉树递归与层序遍历 (Tree Recursion & BFS)

- **LeetCode 104**: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | **[Easy]**
  - 🔑 **考点**: 递归后序遍历 (DFS)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day10_q104_maximum_depth_of_binary_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day10_q104_maximum_depth_of_binary_tree.py)
  - 🧠 **MLSys 底层映射**: 二叉树的递归深度决定了函数系统调用栈的深度。在设计编译器 AST（抽象语法树）解析器和图引擎计算流时，必须理解递归带来的栈内存开销（若树退化为链表，栈深度可达 O(N)）。

- **LeetCode 226**: [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | **[Easy]**
  - 🔑 **考点**: 原地交换子树 (In-place Swap)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day10_q226_invert_binary_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day10_q226_invert_binary_tree.py)
  - 🧠 **MLSys 底层映射**: 典型的二叉树就地结构反转，考察了基础递归函数的返回值处理和就地指针修改机制。

- **LeetCode 102**: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | **[Medium]**
  - 🔑 **考点**: 广度优先搜索 (BFS) + 队列分层
  - 💻 **本地复盘模板**: [sprint_plan/templates/day10_q102_binary_tree_level_order_traversal.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day10_q102_binary_tree_level_order_traversal.py)
  - 🧠 **MLSys 底层映射**: 层序遍历是 BFS 的基础。在图计算引擎和分布式调度系统（如 Ray 调度任务图按依赖层次执行）中，按层推送和合并计算状态是保障时序正确性的通用方案。

---
### 📅 Day 11 - 二叉搜索树与最近公共祖先 (BST & LCA)

- **LeetCode 98**: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | **[Medium]**
  - 🔑 **考点**: BST 偏序区间边界传递
  - 💻 **本地复盘模板**: [sprint_plan/templates/day11_q098_validate_binary_search_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day11_q098_validate_binary_search_tree.py)
  - 🧠 **MLSys 底层映射**: 二叉搜索树的定义是全局偏序的。我们需要在递归过程中不断向下传递每个节点的值必须满足的开区间上限和下限。单纯判定左右子节点是经典的陷阱。

- **LeetCode 235**: [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | **[Medium]**
  - 🔑 **考点**: BST 的数值分岔特性
  - 💻 **本地复盘模板**: [sprint_plan/templates/day11_q235_lowest_common_ancestor_of_a_binary_search_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day11_q235_lowest_common_ancestor_of_a_binary_search_tree.py)
  - 🧠 **MLSys 底层映射**: 若 p 和 q 的值都比当前节点小，往左走；若都比当前节点大，往右走；否则当前节点就是 LCA。借助 BST 性质可以实现 O(H) 时间且 O(1) 空间的最优解。

- **LeetCode 236**: [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | **[Medium]**
  - 🔑 **考点**: 常规二叉树后序回溯
  - 💻 **本地复盘模板**: [sprint_plan/templates/day11_q236_lowest_common_ancestor_of_a_binary_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day11_q236_lowest_common_ancestor_of_a_binary_tree.py)
  - 🧠 **MLSys 底层映射**: 常规二叉树没有大小性质，必须通过 DFS 后序遍历向上传递匹配标志。当左子树和右子树各自返回匹配节点时，当前节点就是最近公共祖先。

---
### 📅 Day 12 - 二叉树构造与路径累加 (Tree Construction & DFS)

- **LeetCode 105**: [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | **[Medium]**
  - 🔑 **考点**: 前中序划分 + 哈希定位 + 递归分治
  - 💻 **本地复盘模板**: [sprint_plan/templates/day12_q105_construct_binary_tree_from_preorder_and_inorder_traversal.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day12_q105_construct_binary_tree_from_preorder_and_inorder_traversal.py)
  - 🧠 **MLSys 底层映射**: 在编译原理的 Parser（解析器）实现中，如何根据 Token 序列和语法中序规则构造语法树是核心任务。通过哈希表缓存中序索引，可以将构造复杂度从 O(N^2) 优化至 O(N)。

- **LeetCode 437**: [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | **[Medium]**
  - 🔑 **考点**: 树上 DFS + 前缀和哈希表
  - 💻 **本地复盘模板**: [sprint_plan/templates/day12_q437_path_sum_iii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day12_q437_path_sum_iii.py)
  - 🧠 **MLSys 底层映射**: 将一维数组的前缀和思想巧妙移植到树结构上。在深度遍历时，用哈希表实时维护从根节点到当前路径的前缀和频数，回溯时清理，实现了 O(N) 时间和 O(H) 空间的高效匹配。

- **LeetCode 124**: [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | **[Hard]**
  - 🔑 **考点**: 后序遍历 + 全局最大值折返更新
  - 💻 **本地复盘模板**: [sprint_plan/templates/day12_q124_binary_tree_maximum_path_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day12_q124_binary_tree_maximum_path_sum.py)
  - 🧠 **MLSys 底层映射**: 树形 DP 的经典代表。在图的计算图关键路径分析（Critical Path Method, CPM - 用于决定多算子计算图中哪个分支执行最慢、是瓶颈）中，折返路径累加算法是寻找系统最慢执行链的基础。

---
### 📅 Day 13 - 回溯与决策搜索空间 (Backtracking basics)

- **LeetCode 78**: [Subsets](https://leetcode.com/problems/subsets/) | **[Medium]**
  - 🔑 **考点**: 递归回溯 / 二进制状态压缩
  - 💻 **本地复盘模板**: [sprint_plan/templates/day13_q078_subsets.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day13_q078_subsets.py)
  - 🧠 **MLSys 底层映射**: 子集生成是典型的决策树生成。在 AI 编译器的算子融合搜索中，我们需要评估所有可能的算子融合子集，并选择最优的执行方式。状态数达 2^N。

- **LeetCode 46**: [Permutations](https://leetcode.com/problems/permutations/) | **[Medium]**
  - 🔑 **考点**: 回溯决策树 + visited 标记
  - 💻 **本地复盘模板**: [sprint_plan/templates/day13_q046_permutations.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day13_q046_permutations.py)
  - 🧠 **MLSys 底层映射**: 全排列代表无重复元素的排列组合问题。用于调度器尝试所有可能的执行顺序以进行指令级别重排优化。

- **LeetCode 39**: [Combination Sum](https://leetcode.com/problems/combination-sum/) | **[Medium]**
  - 🔑 **考点**: 回溯剪枝 + 重复选择控制
  - 💻 **本地复盘模板**: [sprint_plan/templates/day13_q039_combination_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day13_q039_combination_sum.py)
  - 🧠 **MLSys 底层映射**: 组合总和问题。通过传递当前搜索的起始索引指针 `start`，避免生成重复的组合，考察了回溯算法基本的剪枝控重功底。

---
### 📅 Day 14 - 高阶回溯与搜索空间剪枝 (Advanced Backtracking)

- **LeetCode 51**: [N-Queens](https://leetcode.com/problems/n-queens/) | **[Hard]**
  - 🔑 **考点**: 回溯 + 斜线特征数组优化
  - 💻 **本地复盘模板**: [sprint_plan/templates/day14_q051_n_queens.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day14_q051_n_queens.py)
  - 🧠 **MLSys 底层映射**: 经典的 N 皇后回溯。破局点是利用 `r - c` 和 `r + c` 作为对角线的唯一标识数组进行 O(1) 的冲突检测，这比每次扫描棋盘判断冲突高效得多。

- **LeetCode 212**: [Word Search II](https://leetcode.com/problems/word-search-ii/) | **[Hard]**
  - 🔑 **考点**: 前缀树 (Trie) + 二维网格 DFS 回溯 + 状态剪枝
  - 💻 **本地复盘模板**: [sprint_plan/templates/day14_q212_word_search_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day14_q212_word_search_ii.py)
  - 🧠 **MLSys 底层映射**: 在深度搜索时，将待匹配单词列表建成一棵前缀树。在网格 DFS 时同步移动 Trie 指针。更高级的优化是当叶子节点单词被找到后，就地从父节点删除该子树（即叶子剪枝），可让搜索效率大幅提升，避免死路重复搜。

---
## Phase 3: 图论与系统级数据结构 (Day 15-21)
**阶段目标**：通关 BFS/DFS 搜索、有向图拓扑排序、并查集连通性、Trie树优化、双堆中位数实时计算，以及手撕 LRU/LFU 缓存系统。

### 📅 Day 15 - 图的遍历与拓扑连通 (Graph Traversals)

- **LeetCode 200**: [Number of Islands](https://leetcode.com/problems/number-of-islands/) | **[Medium]**
  - 🔑 **考点**: 二维网格 DFS / BFS 连通分量
  - 💻 **本地复盘模板**: [sprint_plan/templates/day15_q200_number_of_islands.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day15_q200_number_of_islands.py)
  - 🧠 **MLSys 底层映射**: 在 MLSys 的张量计算图分割（Compute Graph Partitioning）中，将计算任务切分为多个独立计算子图的逻辑，与寻找岛屿连通块本质相同。原地把 '1' 改为 '0' 可实现空间零开销。

- **LeetCode 133**: [Clone Graph](https://leetcode.com/problems/clone-graph/) | **[Medium]**
  - 🔑 **考点**: 哈希表映射 + DFS/BFS 深拷贝
  - 💻 **本地复盘模板**: [sprint_plan/templates/day15_q133_clone_graph.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day15_q133_clone_graph.py)
  - 🧠 **MLSys 底层映射**: 在编译器中间表示（IR）的优化或深度学习模型序列化中，我们需要完全深拷贝一个包含环路的有向图（如循环神经网络的计算图）。使用哈希表保存 `old_node -> new_node` 的映射，能有效破除环路无限死循环。

- **LeetCode 417**: [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | **[Medium]**
  - 🔑 **考点**: 多源边界逆向 DFS
  - 💻 **本地复盘模板**: [sprint_plan/templates/day15_q417_pacific_atlantic_water_flow.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day15_q417_pacific_atlantic_water_flow.py)
  - 🧠 **MLSys 底层映射**: 逆向思维的代表。如果从每个网格格子出发搜索会超时；从太平洋和大西洋边界向高处逆向“爬坡”遍历，只需 O(M*N) 即可标记出两洋皆可达的交集区域。

---
### 📅 Day 16 - 拓扑排序与计算依赖调度 (Topological Sort)

- **LeetCode 207**: [Course Schedule](https://leetcode.com/problems/course-schedule/) | **[Medium]**
  - 🔑 **考点**:  Kahn 算法 (基于入度的 BFS拓扑排序)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day16_q207_course_schedule.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day16_q207_course_schedule.py)
  - 🧠 **MLSys 底层映射**: 机器学习框架（如 PyTorch、TensorFlow）在执行前向传播和反向传播算子时，算子之间存在严格的输入输出依赖关系，构成了一个 DAG（有向无环图）。编译器正是通过拓扑排序来排定算子执行的先后顺序。

- **LeetCode 210**: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | **[Medium]**
  - 🔑 **考点**: 拓扑排序结果搜集
  - 💻 **本地复盘模板**: [sprint_plan/templates/day16_q210_course_schedule_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day16_q210_course_schedule_ii.py)
  - 🧠 **MLSys 底层映射**: 与 207 题类似，Kahn 算法中节点出队时依次记录，若出队的总节点数等于课程数，则说明无环，返回拓扑序列，否则说明循环依赖，返回空。

- **LeetCode 269**: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | **[Hard]**
  - 🔑 **考点**: 字符邻接表建图 + DFS 环检测 + 拓扑逆序输出
  - 💻 **本地复盘模板**: [sprint_plan/templates/day16_q269_alien_dictionary.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day16_q269_alien_dictionary.py)
  - 🧠 **MLSys 底层映射**: 深度学习编译器中进行多后端算子指令转换时，需要推断各算子执行的绝对偏序关系。通过对比相邻单词推导字符优先级，再跑拓扑排序。

---
### 📅 Day 17 - 并查集与等价类连通 (Union Find)

- **LeetCode 261**: [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | **[Medium]**
  - 🔑 **考点**: 并查集无环检测 & 连通性
  - 💻 **本地复盘模板**: [sprint_plan/templates/day17_q261_graph_valid_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day17_q261_graph_valid_tree.py)
  - 🧠 **MLSys 底层映射**: 并查集是快速合并和检测等价类的数据结构。判断一个无向图是不是一棵树：边数必须等于 `n-1`，且在遍历边合并集合时，如果发现两个点原本就已经属于同一个集合（`find(u) == find(v)`），则说明图中有环，不满足树的定义。

- **LeetCode 323**: [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | **[Medium]**
  - 🔑 **考点**: 并查集合并缩减计数
  - 💻 **本地复盘模板**: [sprint_plan/templates/day17_q323_number_of_connected_components_in_an_undirected_graph.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day17_q323_number_of_connected_components_in_an_undirected_graph.py)
  - 🧠 **MLSys 底层映射**: 初始化连通分量为 n，每次成功合并两个原本不连通的节点，总连通分量 count 减 1。并查集通过路径压缩和按秩合并，操作几乎达到 O(1) 常数级别。

- **LeetCode 684**: [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | **[Medium]**
  - 🔑 **考点**: 并查集定位冗余环路边
  - 💻 **本地复盘模板**: [sprint_plan/templates/day17_q684_redundant_connection.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day17_q684_redundant_connection.py)
  - 🧠 **MLSys 底层映射**: 在冗余网络拓扑或冗余通信路由优化中，找出最后一条导致环路产生的边并剪枝。利用并查集按边顺序处理，首次触发环路的边即为所求。

---
### 📅 Day 18 - 前缀树与高性能词典 (Trie)

- **LeetCode 208**: [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | **[Medium]**
  - 🔑 **考点**: 嵌套哈希结构 / 字符指针字典
  - 💻 **本地复盘模板**: [sprint_plan/templates/day18_q208_implement_trie_prefix_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day18_q208_implement_trie_prefix_tree.py)
  - 🧠 **MLSys 底层映射**: 在大语言模型（LLM）解码生成（LLM Generation）中，推理引擎经常需要利用 Trie 树存储 Token 词表，以进行快速的 Prefix Constraints 搜索或 KV Cache 缓存键值的前缀校验，大幅降低了序列比对的时间。

- **LeetCode 211**: [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | **[Medium]**
  - 🔑 **考点**: Trie 检索 + 通配符多路 DFS 搜索
  - 💻 **本地复盘模板**: [sprint_plan/templates/day18_q211_design_add_and_search_words_data_structure.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day18_q211_design_add_and_search_words_data_structure.py)
  - 🧠 **MLSys 底层映射**: 支持 '.' 通配符的匹配。当遇到 '.' 时，需递归遍历当前节点的所有子分支。体现了前缀树与回溯算法结合的高频操作。

- **LeetCode 642**: [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) | **[Hard]**
  - 🔑 **考点**: Trie 树保存词频 + 最小堆过滤 Top-3
  - 💻 **本地复盘模板**: [sprint_plan/templates/day18_q642_design_search_autocomplete_system.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day18_q642_design_search_autocomplete_system.py)
  - 🧠 **MLSys 底层映射**: 模拟搜索引擎的自动补全。在 LLM 投机采样（Speculative Decoding）或多任务前缀分类中，根据前缀快速过滤和提取高频预测词是核心性能模块。

---
### 📅 Day 19 - 堆与优先队列调度 (Heaps & Schedulers)

- **LeetCode 23**: [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | **[Hard]**
  - 🔑 **考点**: 最小堆动态维护头节点 / 分治合并
  - 💻 **本地复盘模板**: [sprint_plan/templates/day19_q023_merge_k_sorted_lists.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day19_q023_merge_k_sorted_lists.py)
  - 🧠 **MLSys 底层映射**: 在分布式数据流的合并（或流式排序数据块合并）中，使用最小堆来动态跟踪多条有序队列的当前最小头部元素，可以将复杂度控制在 O(N log k)，是大数据处理框架的最核心调度手段。

- **LeetCode 347**: [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | **[Medium]**
  - 🔑 **考点**: 哈希计数 + 频数桶排序 (O(N) 最优解)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day19_q347_top_k_frequent_elements.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day19_q347_top_k_frequent_elements.py)
  - 🧠 **MLSys 底层映射**: 尽管可以用最小堆（O(N log K)）完成，但本题最优雅的解法是利用频数范围在 `[0, N]` 之间的性质，使用桶排序实现 O(N) 的极速检索，体现了根据物理限制优化系统性能的思想。

- **LeetCode 295**: [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | **[Hard]**
  - 🔑 **考点**: 对顶堆平衡 (大顶堆 + 小顶堆)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day19_q295_find_median_from_data_stream.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day19_q295_find_median_from_data_stream.py)
  - 🧠 **MLSys 底层映射**: 在 MLSys 的动态性能剖析器（Performance Profiler）中，我们需要在 $O(1)$ 时间内输出系统吞吐量的中位数，同时以 $O(\log N)$ 接受新吞吐量数据的流入。通过大顶堆维护较小的一半，小顶堆维护较大的一半，通过两个堆顶的动态交互实现了极致平衡。

---
### 📅 Day 20 - 位运算与低精度表示 (Bit Manipulation & Quantization)

- **LeetCode 136**: [Single Number](https://leetcode.com/problems/single-number/) | **[Easy]**
  - 🔑 **考点**: 异或自消去性质 (a ^ a = 0)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day20_q136_single_number.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q136_single_number.py)
  - 🧠 **MLSys 底层映射**: 利用异或运算的自消去（x ^ x = 0，x ^ 0 = x）和交换律结合律，可以实现无额外存储空间查找，是嵌入式设备资源极度受限时常用的数据核对技术。

- **LeetCode 338**: [Counting Bits](https://leetcode.com/problems/counting-bits/) | **[Easy]**
  - 🔑 **考点**: 动态规划 + 位运算偏置转移
  - 💻 **本地复盘模板**: [sprint_plan/templates/day20_q338_counting_bits.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q338_counting_bits.py)
  - 🧠 **MLSys 底层映射**: 利用 `dp[i] = dp[i >> 1] + (i & 1)` 实现在 O(N) 时间内输出大批整数二进制 1 的个数。在神经网络中的二进制网络（Binary Neural Network）或量化权重的位宽统计中，这是基础算子。

- **LeetCode 190**: [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | **[Easy]**
  - 🔑 **考点**: 逐位移位逆转
  - 💻 **本地复盘模板**: [sprint_plan/templates/day20_q190_reverse_bits.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q190_reverse_bits.py)
  - 🧠 **MLSys 底层映射**: 在网络数据包大端序与小端序（Big-endian / Little-endian）转换、或图像底层像素位对齐中，需要将二进制位完全倒置，考察了位运算的基本操作。

- **LeetCode 137**: [Single Number II](https://leetcode.com/problems/single-number-ii/) | **[Medium]**
  - 🔑 **考点**: 二进制各数位求余累加 / 逻辑门电路模拟
  - 💻 **本地复盘模板**: [sprint_plan/templates/day20_q137_single_number_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q137_single_number_ii.py)
  - 🧠 **MLSys 底层映射**: 在 ML 硬件级加速芯片（如 ASIC、FPGA）或 SIMD 指令集优化中，模拟逻辑电路中的状态机转换来对任意 k 周期重复数据进行过滤，是极具代表性的硬件联想题。

---
### 📅 Day 21 - 缓存算法手撕实战 (Cache System Implementation)

- **LeetCode 146**: [LRU Cache](https://leetcode.com/problems/lru-cache/) | **[Medium]**
  - 🔑 **考点**: 哈希表 + 双向循环链表 (O(1) 实战)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day21_q146_lru_cache.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day21_q146_lru_cache.py)
  - 🧠 **MLSys 底层映射**: MLSys 中的核心考点。大模型推理中的 KV Cache 换入换出机制、分布式深度学习参数服务器（Parameter Server）中的冷热权重同步，全部依赖于 LRU 缓存架构。必须能熟练、快速地在白板上实现哈希表与双向链表的就地解耦与重连操作，保证查询和插入均为 O(1)。在面试中，常被追问如何通过读写锁（`shared_mutex`）或细粒度锁使其实现并发安全。

- **LeetCode 460**: [LFU Cache](https://leetcode.com/problems/lfu-cache/) | **[Hard]**
  - 🔑 **考点**: 双哈希表 + 频数链表组织
  - 💻 **本地复盘模板**: [sprint_plan/templates/day21_q460_lfu_cache.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day21_q460_lfu_cache.py)
  - 🧠 **MLSys 底层映射**: 最难的系统级缓存设计题。当空间已满且存在频数冲突时，需淘汰最久未访问（LRU）的节点。需要维护一个 `min_freq` 变量和 {频数: 该频数对应的双向链表} 的哈希表，是极致的数据结构组装挑战。

- **LeetCode 622**: [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | **[Medium]**
  - 🔑 **考点**: 数组环形缓冲区边界指针
  - 💻 **本地复盘模板**: [sprint_plan/templates/day21_q622_design_circular_queue.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day21_q622_design_circular_queue.py)
  - 🧠 **MLSys 底层映射**: 环形缓冲区（Ring Buffer）是操作系统进程间通信（IPC）、生产者-消费者管道、以及 GPU 命令队列（Command Queue）中的核心数据结构。通过 `(tail + 1) % size` 来管理循环写入，实现无锁并发数据交换的基础模型。

---
## Phase 4: 动态规划与全真高压模拟 (Day 22-30)
**阶段目标**：掌握一维/二维 DP 状态转移推导，学会使用剪枝与空间压缩，并在限时高压模拟下克服盲目卡壳。

### 📅 Day 22 - 一维动态规划与拆分决策 (1D DP)

- **LeetCode 70**: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | **[Easy]**
  - 🔑 **考点**: 一维递推 / 滚动变量状态压缩
  - 💻 **本地复盘模板**: [sprint_plan/templates/day22_q070_climbing_stairs.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day22_q070_climbing_stairs.py)
  - 🧠 **MLSys 底层映射**: 动态规划的最简代表。要理解为什么可以用滚动变量（a, b = b, a + b）将空间复杂度从 O(N) 压缩至 O(1)。空间压缩是 MLSys 对海量 Tensor 显存优化的核心追求。

- **LeetCode 746**: [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | **[Easy]**
  - 🔑 **考点**: 带权值的一维递推
  - 💻 **本地复盘模板**: [sprint_plan/templates/day22_q746_min_cost_climbing_stairs.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day22_q746_min_cost_climbing_stairs.py)
  - 🧠 **MLSys 底层映射**: 递推公式 `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`。同样可进行空间压缩优化，是建立 DP 状态转移肌肉记忆的基础。

- **LeetCode 322**: [Coin Change](https://leetcode.com/problems/coin-change/) | **[Medium]**
  - 🔑 **考点**: 完全背包问题自底向上迭代
  - 💻 **本地复盘模板**: [sprint_plan/templates/day22_q322_coin_change.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day22_q322_coin_change.py)
  - 🧠 **MLSys 底层映射**: 无法使用贪心策略求解的最优组合问题。状态转移方程 `dp[i] = min(dp[i], dp[i - coin] + 1)`，初始化为无穷大。在计算资源分配优化中，这种背包分配模型极为常见。

---
### 📅 Day 23 - 子序列与背包模型 (Sequence & Knapsack DP)

- **LeetCode 300**: [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | **[Medium]**
  - 🔑 **考点**:  耐心理牌二分贪心优化 (O(N log N))
  - 💻 **本地复盘模板**: [sprint_plan/templates/day23_q300_longest_increasing_subsequence.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day23_q300_longest_increasing_subsequence.py)
  - 🧠 **MLSys 底层映射**: 最优解是利用辅助数组和二分查找在 O(N log N) 内解决。在编译器做指令流水线优化（Instruction Pipeline - 决定哪些不依赖的指令可以并行发射）中，寻找最长单调序列可以为指令重排提供直接依据。

- **LeetCode 139**: [Word Break](https://leetcode.com/problems/word-break/) | **[Medium]**
  - 🔑 **考点**: 前缀切分 DP + 字典 Set 高速查找
  - 💻 **本地复盘模板**: [sprint_plan/templates/day23_q139_word_break.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day23_q139_word_break.py)
  - 🧠 **MLSys 底层映射**: 判断一段连续流是否可以被有效切分。状态转移为 `dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`。在 NLP 分词及算子大图切分生成中，这种前缀切分逻辑扮演重要角色。

- **LeetCode 416**: [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | **[Medium]**
  - 🔑 **考点**: 0-1 背包问题状态压缩
  - 💻 **本地复盘模板**: [sprint_plan/templates/day23_q416_partition_equal_subset_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day23_q416_partition_equal_subset_sum.py)
  - 🧠 **MLSys 底层映射**: 典型的 0-1 背包。为了防止空间溢出，我们需要使用从右往左的一维 DP 倒序更新，将空间复杂度降到 O(target)。在分布式计算中，任务划分以实现负载均衡通常可退化为此类背包分割。

---
### 📅 Day 24 - 二维动态规划与网格状态 (2D DP)

- **LeetCode 62**: [Unique Paths](https://leetcode.com/problems/unique-paths/) | **[Medium]**
  - 🔑 **考点**: 二维网格自上自左累加 / 一维行滚动压缩
  - 💻 **本地复盘模板**: [sprint_plan/templates/day24_q062_unique_paths.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day24_q062_unique_paths.py)
  - 🧠 **MLSys 底层映射**: 经典的网格路线规划。状态转移 `dp[i][j] = dp[i-1][j] + dp[i][j-1]`。在物理芯片的二维网格布线（NoC - Network on Chip 芯片上路由器数据路由设计）中，分析路由包的流动路径概率与此模型高度重合。可做一维行空间压缩。

- **LeetCode 1143**: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | **[Medium]**
  - 🔑 **考点**: 二维子序列比对矩阵
  - 💻 **本地复盘模板**: [sprint_plan/templates/day24_q1143_longest_common_subsequence.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day24_q1143_longest_common_subsequence.py)
  - 🧠 **MLSys 底层映射**: 在比较两个大规模神经网络结构差异（或两份编译代码相似度 Diff 工具）时，LCS 是核心底层比对算法。时间复杂度为 O(M*N)，通常会涉及空间维度的滚动压缩面试追问。

- **LeetCode 72**: [Edit Distance](https://leetcode.com/problems/edit-distance/) | **[Hard]**
  - 🔑 **考点**: 二维操作决策 (插入、删除、替换)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day24_q072_edit_distance.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day24_q072_edit_distance.py)
  - 🧠 **MLSys 底层映射**: 字符编辑的最佳路径代价计算。通过分析三种状态来源 `dp[i-1][j]`、`dp[i][j-1]` 和 `dp[i-1][j-1]` 构造全局转移网格。是高阶 DP 状态分析功底的试金石。

---
### 📅 Day 25 - 区间与树形动态规划 (Interval & Tree DP)

- **LeetCode 96**: [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | **[Medium]**
  - 🔑 **考点**: 卡特兰数 (Catalan Number) 递推
  - 💻 **本地复盘模板**: [sprint_plan/templates/day25_q096_unique_binary_search_trees.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day25_q096_unique_binary_search_trees.py)
  - 🧠 **MLSys 底层映射**: 统计所有可能生成的 BST 数量。通过累加左子树可能数与右子树可能数的乘积，推导出递推关系式。展示了状态划分的数学对称性。

- **LeetCode 337**: [House Robber III](https://leetcode.com/problems/house-robber-iii/) | **[Medium]**
  - 🔑 **考点**: 树形 DP + 节点状态元组传递
  - 💻 **本地复盘模板**: [sprint_plan/templates/day25_q337_house_robber_iii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day25_q337_house_robber_iii.py)
  - 🧠 **MLSys 底层映射**: 在计算图（Computational Graph）的算子融合选择中，如果相邻的算子不能同时参与某种全局优化，那么最大优化收益的计算就是典型的树形 DP。DFS 返回 `(抢当前节点的最大值, 不抢当前节点的最大值)` 的元组，将复杂度限制在完美的 O(N)。

- **LeetCode 312**: [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | **[Hard]**
  - 🔑 **考点**: 区间 DP / 自底向上填表
  - 💻 **本地复盘模板**: [sprint_plan/templates/day25_q312_burst_balloons.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day25_q312_burst_balloons.py)
  - 🧠 **MLSys 底层映射**: 区间 DP 巅峰。通过逆向思考“哪一个气球是最后一个被戳破的”，将大区间分割为两个独立子区间加额外收益，从而写出状态转移方程。主要在复杂的算子串联调度优化中作为数学底座。

---
### 📅 Day 26 - 贪心决策与区间调度 (Greedy Algorithms)

- **LeetCode 55**: [Jump Game](https://leetcode.com/problems/jump-game/) | **[Medium]**
  - 🔑 **考点**: 贪心策略 - 自后向前更新 goal
  - 💻 **本地复盘模板**: [sprint_plan/templates/day26_q055_jump_game.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day26_q055_jump_game.py)
  - 🧠 **MLSys 底层映射**: 在资源管理中判定任务能否在一系列具有最大跳转能力的节点间安全传递。自后向前维护当前的“最前可达点” goal，时间复杂度 O(N)，空间复杂度 O(1)，大幅优于一维 DP 的 O(N^2) 方案。

- **LeetCode 134**: [Gas Station](https://leetcode.com/problems/gas-station/) | **[Medium]**
  - 🔑 **考点**: 总余量判定 + 起点自前向后移位
  - 💻 **本地复盘模板**: [sprint_plan/templates/day26_q134_gas_station.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day26_q134_gas_station.py)
  - 🧠 **MLSys 底层映射**: 如果总加油量大于总消耗量，必然有解。通过一次遍历，一旦当前油量归负就将起点设为下一站，巧妙地将 O(N^2) 查找降至 O(N) 贪心决策。

- **LeetCode 406**: [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | **[Medium]**
  - 🔑 **考点**: 排序 + 贪心插入位置
  - 💻 **本地复盘模板**: [sprint_plan/templates/day26_q406_queue_reconstruction_by_height.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day26_q406_queue_reconstruction_by_height.py)
  - 🧠 **MLSys 底层映射**: 在多资源争抢的优先级队列调度中，根据两个维度的权重动态安排优先级。通过先降序排高度、再按 K 索引插入的方法，实现了局部的最优队列重构。

---
### 📅 Day 27 - 区间重叠与多维度调度 (Intervals & Scheduling)

- **LeetCode 56**: [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | **[Medium]**
  - 🔑 **考点**: 起点排序 + 顺序区间合并
  - 💻 **本地复盘模板**: [sprint_plan/templates/day27_q056_merge_intervals.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day27_q056_merge_intervals.py)
  - 🧠 **MLSys 底层映射**: 在操作系统的物理内存分配器中，当多个虚拟页面被释放时，我们需要将相邻且相接的空闲内存区间进行“物理合并”，以减少系统内存碎片。这个合并的核心逻辑就是区间合并。

- **LeetCode 435**: [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | **[Medium]**
  - 🔑 **考点**: 贪心策略 - 终点排序优先保留先结束区间
  - 💻 **本地复盘模板**: [sprint_plan/templates/day27_q435_non_overlapping_intervals.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day27_q435_non_overlapping_intervals.py)
  - 🧠 **MLSys 底层映射**: 经典的区间调度问题。为了给后面留出尽可能多的调度空间，应当优先保留结束时间最早的区间。常用于高并发事件调度器和算子流水线调度中。

- **LeetCode 621**: [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | **[Medium]**
  - 🔑 **考点**: 桶模型贪心 / 冷却时间公式计算
  - 💻 **本地复盘模板**: [sprint_plan/templates/day27_q621_task_scheduler.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day27_q621_task_scheduler.py)
  - 🧠 **MLSys 底层映射**: 在操作系统的 CPU 核心任务调度或 GPU 算子多通道流水发射中，相同类型的任务必须间隔一定的 Cooldown 冷却时间才能再次发射。通过统计最高频任务填充桶的方法，可实现在 O(N) 时间内计算出最小执行总周期。

---
### 📅 Day 28 - 全真高压模拟 Day 1 (Google/Meta 偏底层高频真题)

- **LeetCode 307**: [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d---mutable/) | **[Hard]**
  - 🔑 **考点**: 树状数组 (Binary Indexed Tree / Fenwick Tree) / 线段树
  - 💻 **本地复盘模板**: [sprint_plan/templates/day28_q307_range_sum_query_2d___mutable.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day28_q307_range_sum_query_2d___mutable.py)
  - 🧠 **MLSys 底层映射**: 在动态 ML 算子中，当局部权重频繁被修改（Mutable），且同时需要频繁查询区域总和时，普通前缀和会导致修改代价高达 O(N)。使用树状数组，可使得单点更新和区域查询的复杂度均为完美的 O(log N)，体现了高级系统的折中优化。

- **LeetCode 588**: [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) | **[Hard]**
  - 🔑 **考点**: Trie 树扩展节点设计 + 目录树 DFS
  - 💻 **本地复盘模板**: [sprint_plan/templates/day28_q588_design_in_memory_file_system.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day28_q588_design_in_memory_file_system.py)
  - 🧠 **MLSys 底层映射**: 手撕内存文件系统。核心是设计一个包含 {子目录名: 节点} 且叶子节点能存储具体文件内容的 Trie 树，支持 `ls`, `mkdir`, `addContentToFile`, `readContentFromFile` 等操作。考查了高并发操作系统底层模拟构建。

---
### 📅 Day 29 - 全真高压模拟 Day 2 (NVIDIA/Apple 硬件与并发关联真题)

- **LeetCode 311**: [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) | **[Medium]**
  - 🔑 **考点**: 稀疏表示行主序非零遍历优化 (CRS / CSR 压缩格式)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day29_q311_sparse_matrix_multiplication.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day29_q311_sparse_matrix_multiplication.py)
  - 🧠 **MLSys 底层映射**: 深度学习中稀疏神经网络（Sparse Neural Network）计算的绝对核心。在 GPU 计算中，如果直接对大量为 0 的节点做密集乘法会极度浪费带宽和算力。使用行主序只对非零节点进行累加运算，极大地模拟了 CSR 格式的硬件加速逻辑。

- **LeetCode 380**: [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | **[Medium]**
  - 🔑 **考点**: 哈希表 + 动态数组交换尾部元素删除
  - 💻 **本地复盘模板**: [sprint_plan/templates/day29_q380_insert_delete_getrandom_o1.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day29_q380_insert_delete_getrandom_o1.py)
  - 🧠 **MLSys 底层映射**: 很多 MLSys 的负采样（Negative Sampling）中需要在 O(1) 内随机抽取样本，同时支持 O(1) 的插入和删除。哈希表做映射，数组存储实际元素。删除时将目标与数组尾部元素交换再 pop_back，避免了数组搬移开销。

---
### 📅 Day 30 - 全真高压模拟 Day 3 (大厂 Hard 极客挑战终局模拟)

- **LeetCode 460**: [LFU Cache](https://leetcode.com/problems/lfu-cache/) | **[Hard]**
  - 🔑 **考点**: 手撕 LFU (复习 Day 21)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day30_q460_lfu_cache.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day30_q460_lfu_cache.py)
  - 🧠 **MLSys 底层映射**: 在高并发网关及存储引擎底层，淘汰频率最低的缓存节点。在高压限时下，必须做到双哈希表和双向链表操作行云流水无 Bug。

- **LeetCode 212**: [Word Search II](https://leetcode.com/problems/word-search-ii/) | **[Hard]**
  - 🔑 **考点**: 手撕 Trie + Grid DFS (复习 Day 14)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day30_q212_word_search_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day30_q212_word_search_ii.py)
  - 🧠 **MLSys 底层映射**: 综合考察前缀树、矩阵 DFS、回溯算法和叶子树枝剪枝优化，是考察复杂路径探索的压轴题。

- **LeetCode 269**: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | **[Hard]**
  - 🔑 **考点**: 手撕拓扑排序有向图环检测 (复习 Day 16)
  - 💻 **本地复盘模板**: [sprint_plan/templates/day30_q269_alien_dictionary.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day30_q269_alien_dictionary.py)
  - 🧠 **MLSys 底层映射**: 系统编译调度的基石，将输入依赖解析、建图、环检测、拓扑排序汇于一体，极其考验白板代码的完整度和鲁棒性。

---