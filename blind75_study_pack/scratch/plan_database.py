# -*- coding: utf-8 -*-

PHASES = [
    {
        "name": "Phase 1: 基础与指针直觉 (Day 1-7)",
        "target": "掌握左右双指针、快慢指针、滑动窗口、单调栈等核心模板，建立数组与链表肌肉记忆，戒掉低级指针越界Bug。",
        "days": {
            1: {
                "theme": "数组与双指针 (Array & Two Pointers)",
                "problems": [
                    {"id": "1", "name": "Two Sum", "difficulty": "Easy", "key": "哈希表 / 双指针", "systems_note": "在系统底层或 GPU 算子设计中，利用静态哈希映射或有序双指针进行匹配是快速查表的最基本手段。时间复杂度从 O(N^2) 降至 O(N)，属于空间换时间的典范。"},
                    {"id": "15", "name": "3Sum", "difficulty": "Medium", "key": "排序 + 双指针左右逼近", "systems_note": "左右双指针的核心是利用单调性进行状态缩减。通过排序，使得我们可以利用单调性移动两端指针，避免暴力三层循环。"},
                    {"id": "11", "name": "Container With Most Water", "difficulty": "Medium", "key": "双指针 + 贪心移动短板", "systems_note": "贪心策略在分布式系统的调度决策（例如最少网络开销节点选择）中极为常见。移动高度低的一侧是唯一能让后续面积增大的可能。"}
                ]
            },
            2: {
                "theme": "滑动窗口 (Sliding Window)",
                "problems": [
                    {"id": "3", "name": "Longest Substring Without Repeating Characters", "difficulty": "Medium", "key": "双指针滑动窗口 + 哈希集合", "systems_note": "滑动窗口用于处理连续子区间问题。在网络协议层（例如 TCP 滑动窗口接收缓冲区管理）和流处理系统（比如计算过去 10s 的平均推理请求率）中，这是基本的操作模式。"},
                    {"id": "424", "name": "Longest Repeating Character Replacement", "difficulty": "Medium", "key": "滑动窗口 + 局部频数统计优化", "systems_note": "窗口大小 L 减去出现最多的字符频数 max_freq 必须小于等于 k。通过维护历史最大频数 max_freq 避免了在窗口收缩时重新统计频数的 O(26) 扫描。"},
                    {"id": "76", "name": "Minimum Window Substring", "difficulty": "Hard", "key": "双哈希表计数 + 最优窗口收缩", "systems_note": "Hard 级别的滑动窗口标杆。在编译器词法分析（Lexical Analysis）和编译器底层字符串匹配扫描器中，此类逻辑经常被用来作为高性能语法解析的核心组件。"}
                ]
            },
            3: {
                "theme": "快慢指针与循环检测 (Fast & Slow Pointers)",
                "problems": [
                    {"id": "141", "name": "Linked List Cycle", "difficulty": "Easy", "key": "快慢指针 (Floyd 判圈算法)", "systems_note": "快慢指针在内存管理器中用来判断数据块链表（比如堆内存块分配链表）是否因越界或 Bug 发生了指针环形闭合，是基础防爆内存工具。"},
                    {"id": "142", "name": "Linked List Cycle II", "difficulty": "Medium", "key": "快慢指针寻找环起点", "systems_note": "数学推导：从头节点到环起点的距离等于快慢指针相遇点到环起点的距离。本题展示了指针距离计算的绝对控制能力。"},
                    {"id": "202", "name": "Happy Number", "difficulty": "Easy", "key": "隐式链表判圈", "systems_note": "数字变换过程可抽象为隐式有向图中的单链表。当变换陷入死循环时，即可使用快慢指针检测，无需借助哈希表，实现 O(1) 空间占用。"}
                ]
            },
            4: {
                "theme": "单调栈与边界判定 (Monotonic Stack)",
                "problems": [
                    {"id": "496", "name": "Next Greater Element I", "difficulty": "Easy", "key": "单调递减栈", "systems_note": "单调栈是解决 '寻找下一个更大元素' 问题的利器。通过栈的单调性，我们可以保证每个元素仅入栈出栈一次，实现时间复杂度 O(N)。"},
                    {"id": "739", "name": "Daily Temperatures", "difficulty": "Medium", "key": "单调递减栈保存索引", "systems_note": "在时间轴分析与系统性能指标监控（如计算延迟首次下降的天数）中，基于单调栈的后向距离计算是经典的流处理计算节点结构。"},
                    {"id": "84", "name": "Largest Rectangle in Histogram", "difficulty": "Hard", "key": "单调递增栈 + 哨兵节点", "systems_note": "系统内存碎片的合并计算（如寻址连续物理页面的最大矩阵）中，此算法提供了 O(N) 的极速求解器。对栈顶弹出的高板计算面积是核心。"}
                ]
            },
            5: {
                "theme": "单调队列与滑动指标 (Monotonic Queue)",
                "problems": [
                    {"id": "239", "name": "Sliding Window Maximum", "difficulty": "Hard", "key": "单调队列 (双端队列 deque)", "systems_note": "在 MLSys 的推理服务器中，我们需要计算滑动时间窗口内的最大推理耗时或吞吐量。基于双端队列的单调队列算法，保证每个元素入队出队最多一次，实现了完美的 O(N) 实时监控统计。"},
                    {"id": "862", "name": "Shortest Subarray with Sum at Least K", "difficulty": "Hard", "key": "前缀和 + 单调双端队列", "systems_note": "在包含负值的数据流中寻找满足累加阈值的最短子区间。利用前缀和与单调递增队列，可在 O(N) 时间内完成最优区间检索。"}
                ]
            },
            6: {
                "theme": "前缀和与差分数组 (Prefix Sums & Difference Arrays)",
                "problems": [
                    {"id": "304", "name": "Range Sum Query 2D - Immutable", "difficulty": "Medium", "key": "二维前缀和积分图", "systems_note": "二维前缀和本质上是计算机视觉和图像处理中的“积分图 (Integral Image)”。在 CNN（卷积神经网络）的池化层或局部求和加速中，利用前缀和可以将任何局部区间求和的复杂度从 O(H*W) 直接降至 O(1)。"},
                    {"id": "1109", "name": "Corporate Flight Bookings", "difficulty": "Medium", "key": "一维差分数组", "systems_note": "差分数组用于高效处理“区间批量加减运算”。在系统调度中，如果要在某个时间区间内给所有任务分配相同的算力资源，使用差分数组可实现 O(1) 的记录，并在最后通过一次前缀和扫描还原，复杂度为 O(N)。"},
                    {"id": "1094", "name": "Car Pooling", "difficulty": "Medium", "key": "差分数组检验超载边界", "systems_note": "在分布式系统的并发容量限制（或 GPU 显存分配动态阈值）检测中，将区间分配需求转换为差分数组来一曲校验最大并发数是否超标，是极佳的调度前置步骤。"}
                ]
            },
            7: {
                "theme": "矩阵变换与缓存局部性 (Matrix Operations & Locality)",
                "problems": [
                    {"id": "48", "name": "Rotate Image", "difficulty": "Medium", "key": "矩阵原地转置 + 水平翻转", "systems_note": "转置和反转的操作完全符合计算机系统结构中“缓存局部性 (Cache Locality)”的考察。在 MLSys 底层中，Tensor 维度的置换（Transpose/Permute）是高频算子，如何实现一维连续内存的高速 stride 寻址和原地调换是 GPU 算子优化的核心。"},
                    {"id": "54", "name": "Spiral Matrix", "difficulty": "Medium", "key": "边界指针收缩模拟", "systems_note": "模拟螺旋轨迹访问。对边界条件（上、下、左、右）进行严格的动态收缩，考察了面试中对大矩阵边界控制无 Bug 编写的基本功。"},
                    {"id": "73", "name": "Set Matrix Zeroes", "difficulty": "Medium", "key": "首行首列作为状态标记器", "systems_note": "内存极度受限时的空间优化方案。通过把中间元素的置零标记投影到矩阵第一行和第一列，实现了 O(1) 的额外空间复杂度。在嵌入式或边缘设备算子中极为实用。"}
                ]
            }
        }
    },
    {
        "name": "Phase 2: 树与二分查找 (Day 8-14)",
        "target": "突破二分查找边界控制（防死循环），精通二叉树与 BST 性质的递归推导，克服递归恐惧。",
        "days": {
            8: {
                "theme": "二分查找与折半搜索 (Binary Search)",
                "problems": [
                    {"id": "704", "name": "Binary Search", "difficulty": "Easy", "key": "标准二分查找模板", "systems_note": "二分查找的精髓在于边界区间的划分与防死循环条件。在底层系统设计中，诸如内存页表快速检索、有序键值对存储的检索，二分查找是必不可少的 O(log N) 算法。"},
                    {"id": "33", "name": "Search in Rotated Sorted Array", "difficulty": "Medium", "key": "分段单调性二分查找", "systems_note": "经典的旋转数组检索。核心破局点是：如果从中间剖开，旋转有序数组的左右两半必然有一半是严格升序的。通过判断哪半边有序，可以照样将搜索范围折半。"},
                    {"id": "153", "name": "Find Minimum in Rotated Sorted Array", "difficulty": "Medium", "key": "二分收缩旋转点", "systems_note": "与右边界 nums[right] 对比。如果 nums[mid] > nums[right] 说明最小值在右侧；否则在左侧。考察了在非经典升序数组中发掘单调性进行二分收缩的能力。"}
                ]
            },
            9: {
                "theme": "二分查找进阶与实数域 (Advanced Binary Search)",
                "problems": [
                    {"id": "74", "name": "Search a 2D Matrix", "difficulty": "Medium", "key": "二维矩阵一维化二分", "systems_note": "行优先存储（Row-major order）的二维矩阵在内存中是一维连续存储的。通过逻辑上的映射 `(row, col) = (mid // n, mid % n)`，可以直接在连续内存上跑标准二分，避免昂贵的行转换开销。"},
                    {"id": "162", "name": "Find Peak Element", "difficulty": "Medium", "key": "寻找局部峰值 / 爬坡法", "systems_note": "在机器学习的最优化理论和系统的自适应参数调节中，“爬坡法（Hill Climbing）”是搜索局部最优的基本手段。只要当前位置处于上升趋势，则峰值必然在右侧，从而实现 O(log N) 局部峰值定位。"},
                    {"id": "4", "name": "Median of Two Sorted Arrays", "difficulty": "Hard", "key": "双数组划分 + 对角二分", "systems_note": "在分布式数据库或多机多卡 Tensor 拆分中，经常需要对两个异构且分别有序的数据块进行合并定位中位数。利用二分较小数组划分线的方法，可在 O(log(min(M, N))) 时间内精确分割。"}
                ]
            },
            10: {
                "theme": "二叉树递归与层序遍历 (Tree Recursion & BFS)",
                "problems": [
                    {"id": "104", "name": "Maximum Depth of Binary Tree", "difficulty": "Easy", "key": "递归后序遍历 (DFS)", "systems_note": "二叉树的递归深度决定了函数系统调用栈的深度。在设计编译器 AST（抽象语法树）解析器和图引擎计算流时，必须理解递归带来的栈内存开销（若树退化为链表，栈深度可达 O(N)）。"},
                    {"id": "226", "name": "Invert Binary Tree", "difficulty": "Easy", "key": "原地交换子树 (In-place Swap)", "systems_note": "典型的二叉树就地结构反转，考察了基础递归函数的返回值处理和就地指针修改机制。"},
                    {"id": "102", "name": "Binary Tree Level Order Traversal", "difficulty": "Medium", "key": "广度优先搜索 (BFS) + 队列分层", "systems_note": "层序遍历是 BFS 的基础。在图计算引擎和分布式调度系统（如 Ray 调度任务图按依赖层次执行）中，按层推送和合并计算状态是保障时序正确性的通用方案。"}
                ]
            },
            11: {
                "theme": "二叉搜索树与最近公共祖先 (BST & LCA)",
                "problems": [
                    {"id": "98", "name": "Validate Binary Search Tree", "difficulty": "Medium", "key": "BST 偏序区间边界传递", "systems_note": "二叉搜索树的定义是全局偏序的。我们需要在递归过程中不断向下传递每个节点的值必须满足的开区间上限和下限。单纯判定左右子节点是经典的陷阱。"},
                    {"id": "235", "name": "Lowest Common Ancestor of a Binary Search Tree", "difficulty": "Medium", "key": "BST 的数值分岔特性", "systems_note": "若 p 和 q 的值都比当前节点小，往左走；若都比当前节点大，往右走；否则当前节点就是 LCA。借助 BST 性质可以实现 O(H) 时间且 O(1) 空间的最优解。"},
                    {"id": "236", "name": "Lowest Common Ancestor of a Binary Tree", "difficulty": "Medium", "key": "常规二叉树后序回溯", "systems_note": "常规二叉树没有大小性质，必须通过 DFS 后序遍历向上传递匹配标志。当左子树和右子树各自返回匹配节点时，当前节点就是最近公共祖先。"}
                ]
            },
            12: {
                "theme": "二叉树构造与路径累加 (Tree Construction & DFS)",
                "problems": [
                    {"id": "105", "name": "Construct Binary Tree from Preorder and Inorder Traversal", "difficulty": "Medium", "key": "前中序划分 + 哈希定位 + 递归分治", "systems_note": "在编译原理的 Parser（解析器）实现中，如何根据 Token 序列和语法中序规则构造语法树是核心任务。通过哈希表缓存中序索引，可以将构造复杂度从 O(N^2) 优化至 O(N)。"},
                    {"id": "437", "name": "Path Sum III", "difficulty": "Medium", "key": "树上 DFS + 前缀和哈希表", "systems_note": "将一维数组的前缀和思想巧妙移植到树结构上。在深度遍历时，用哈希表实时维护从根节点到当前路径的前缀和频数，回溯时清理，实现了 O(N) 时间和 O(H) 空间的高效匹配。"},
                    {"id": "124", "name": "Binary Tree Maximum Path Sum", "difficulty": "Hard", "key": "后序遍历 + 全局最大值折返更新", "systems_note": "树形 DP 的经典代表。在图的计算图关键路径分析（Critical Path Method, CPM - 用于决定多算子计算图中哪个分支执行最慢、是瓶颈）中，折返路径累加算法是寻找系统最慢执行链的基础。"}
                ]
            },
            13: {
                "theme": "回溯与决策搜索空间 (Backtracking basics)",
                "problems": [
                    {"id": "78", "name": "Subsets", "difficulty": "Medium", "key": "递归回溯 / 二进制状态压缩", "systems_note": "子集生成是典型的决策树生成。在 AI 编译器的算子融合搜索中，我们需要评估所有可能的算子融合子集，并选择最优的执行方式。状态数达 2^N。"},
                    {"id": "46", "name": "Permutations", "difficulty": "Medium", "key": "回溯决策树 + visited 标记", "systems_note": "全排列代表无重复元素的排列组合问题。用于调度器尝试所有可能的执行顺序以进行指令级别重排优化。"},
                    {"id": "39", "name": "Combination Sum", "difficulty": "Medium", "key": "回溯剪枝 + 重复选择控制", "systems_note": "组合总和问题。通过传递当前搜索的起始索引指针 `start`，避免生成重复的组合，考察了回溯算法基本的剪枝控重功底。"}
                ]
            },
            14: {
                "theme": "高阶回溯与搜索空间剪枝 (Advanced Backtracking)",
                "problems": [
                    {"id": "51", "name": "N-Queens", "difficulty": "Hard", "key": "回溯 + 斜线特征数组优化", "systems_note": "经典的 N 皇后回溯。破局点是利用 `r - c` 和 `r + c` 作为对角线的唯一标识数组进行 O(1) 的冲突检测，这比每次扫描棋盘判断冲突高效得多。"},
                    {"id": "212", "name": "Word Search II", "difficulty": "Hard", "key": "前缀树 (Trie) + 二维网格 DFS 回溯 + 状态剪枝", "systems_note": "在深度搜索时，将待匹配单词列表建成一棵前缀树。在网格 DFS 时同步移动 Trie 指针。更高级的优化是当叶子节点单词被找到后，就地从父节点删除该子树（即叶子剪枝），可让搜索效率大幅提升，避免死路重复搜。"}
                ]
            }
        }
    },
    {
        "name": "Phase 3: 图论与系统级数据结构 (Day 15-21)",
        "target": "通关 BFS/DFS 搜索、有向图拓扑排序、并查集连通性、Trie树优化、双堆中位数实时计算，以及手撕 LRU/LFU 缓存系统。",
        "days": {
            15: {
                "theme": "图的遍历与拓扑连通 (Graph Traversals)",
                "problems": [
                    {"id": "200", "name": "Number of Islands", "difficulty": "Medium", "key": "二维网格 DFS / BFS 连通分量", "systems_note": "在 MLSys 的张量计算图分割（Compute Graph Partitioning）中，将计算任务切分为多个独立计算子图的逻辑，与寻找岛屿连通块本质相同。原地把 '1' 改为 '0' 可实现空间零开销。"},
                    {"id": "133", "name": "Clone Graph", "difficulty": "Medium", "key": "哈希表映射 + DFS/BFS 深拷贝", "systems_note": "在编译器中间表示（IR）的优化或深度学习模型序列化中，我们需要完全深拷贝一个包含环路的有向图（如循环神经网络的计算图）。使用哈希表保存 `old_node -> new_node` 的映射，能有效破除环路无限死循环。"},
                    {"id": "417", "name": "Pacific Atlantic Water Flow", "difficulty": "Medium", "key": "多源边界逆向 DFS", "systems_note": "逆向思维的代表。如果从每个网格格子出发搜索会超时；从太平洋和大西洋边界向高处逆向“爬坡”遍历，只需 O(M*N) 即可标记出两洋皆可达的交集区域。"}
                ]
            },
            16: {
                "theme": "拓扑排序与计算依赖调度 (Topological Sort)",
                "problems": [
                    {"id": "207", "name": "Course Schedule", "difficulty": "Medium", "key": " Kahn 算法 (基于入度的 BFS拓扑排序)", "systems_note": "机器学习框架（如 PyTorch、TensorFlow）在执行前向传播和反向传播算子时，算子之间存在严格的输入输出依赖关系，构成了一个 DAG（有向无环图）。编译器正是通过拓扑排序来排定算子执行的先后顺序。"},
                    {"id": "210", "name": "Course Schedule II", "difficulty": "Medium", "key": "拓扑排序结果搜集", "systems_note": "与 207 题类似，Kahn 算法中节点出队时依次记录，若出队的总节点数等于课程数，则说明无环，返回拓扑序列，否则说明循环依赖，返回空。"},
                    {"id": "269", "name": "Alien Dictionary", "difficulty": "Hard", "key": "字符邻接表建图 + DFS 环检测 + 拓扑逆序输出", "systems_note": "深度学习编译器中进行多后端算子指令转换时，需要推断各算子执行的绝对偏序关系。通过对比相邻单词推导字符优先级，再跑拓扑排序。"}
                ]
            },
            17: {
                "theme": "并查集与等价类连通 (Union Find)",
                "problems": [
                    {"id": "261", "name": "Graph Valid Tree", "difficulty": "Medium", "key": "并查集无环检测 & 连通性", "systems_note": "并查集是快速合并和检测等价类的数据结构。判断一个无向图是不是一棵树：边数必须等于 `n-1`，且在遍历边合并集合时，如果发现两个点原本就已经属于同一个集合（`find(u) == find(v)`），则说明图中有环，不满足树的定义。"},
                    {"id": "323", "name": "Number of Connected Components in an Undirected Graph", "difficulty": "Medium", "key": "并查集合并缩减计数", "systems_note": "初始化连通分量为 n，每次成功合并两个原本不连通的节点，总连通分量 count 减 1。并查集通过路径压缩和按秩合并，操作几乎达到 O(1) 常数级别。"},
                    {"id": "684", "name": "Redundant Connection", "difficulty": "Medium", "key": "并查集定位冗余环路边", "systems_note": "在冗余网络拓扑或冗余通信路由优化中，找出最后一条导致环路产生的边并剪枝。利用并查集按边顺序处理，首次触发环路的边即为所求。"}
                ]
            },
            18: {
                "theme": "前缀树与高性能词典 (Trie)",
                "problems": [
                    {"id": "208", "name": "Implement Trie (Prefix Tree)", "difficulty": "Medium", "key": "嵌套哈希结构 / 字符指针字典", "systems_note": "在大语言模型（LLM）解码生成（LLM Generation）中，推理引擎经常需要利用 Trie 树存储 Token 词表，以进行快速的 Prefix Constraints 搜索或 KV Cache 缓存键值的前缀校验，大幅降低了序列比对的时间。"},
                    {"id": "211", "name": "Design Add and Search Words Data Structure", "difficulty": "Medium", "key": "Trie 检索 + 通配符多路 DFS 搜索", "systems_note": "支持 '.' 通配符的匹配。当遇到 '.' 时，需递归遍历当前节点的所有子分支。体现了前缀树与回溯算法结合的高频操作。"},
                    {"id": "642", "name": "Design Search Autocomplete System", "difficulty": "Hard", "key": "Trie 树保存词频 + 最小堆过滤 Top-3", "systems_note": "模拟搜索引擎的自动补全。在 LLM 投机采样（Speculative Decoding）或多任务前缀分类中，根据前缀快速过滤和提取高频预测词是核心性能模块。"}
                ]
            },
            19: {
                "theme": "堆与优先队列调度 (Heaps & Schedulers)",
                "problems": [
                    {"id": "23", "name": "Merge k Sorted Lists", "difficulty": "Hard", "key": "最小堆动态维护头节点 / 分治合并", "systems_note": "在分布式数据流的合并（或流式排序数据块合并）中，使用最小堆来动态跟踪多条有序队列的当前最小头部元素，可以将复杂度控制在 O(N log k)，是大数据处理框架的最核心调度手段。"},
                    {"id": "347", "name": "Top K Frequent Elements", "difficulty": "Medium", "key": "哈希计数 + 频数桶排序 (O(N) 最优解)", "systems_note": "尽管可以用最小堆（O(N log K)）完成，但本题最优雅的解法是利用频数范围在 `[0, N]` 之间的性质，使用桶排序实现 O(N) 的极速检索，体现了根据物理限制优化系统性能的思想。"},
                    {"id": "295", "name": "Find Median from Data Stream", "difficulty": "Hard", "key": "对顶堆平衡 (大顶堆 + 小顶堆)", "systems_note": "在 MLSys 的动态性能剖析器（Performance Profiler）中，我们需要在 $O(1)$ 时间内输出系统吞吐量的中位数，同时以 $O(\\log N)$ 接受新吞吐量数据的流入。通过大顶堆维护较小的一半，小顶堆维护较大的一半，通过两个堆顶的动态交互实现了极致平衡。"}
                ]
            },
            20: {
                "theme": "位运算与低精度表示 (Bit Manipulation & Quantization)",
                "problems": [
                    {"id": "136", "name": "Single Number", "difficulty": "Easy", "key": "异或自消去性质 (a ^ a = 0)", "systems_note": "利用异或运算的自消去（x ^ x = 0，x ^ 0 = x）和交换律结合律，可以实现无额外存储空间查找，是嵌入式设备资源极度受限时常用的数据核对技术。"},
                    {"id": "338", "name": "Counting Bits", "difficulty": "Easy", "key": "动态规划 + 位运算偏置转移", "systems_note": "利用 `dp[i] = dp[i >> 1] + (i & 1)` 实现在 O(N) 时间内输出大批整数二进制 1 的个数。在神经网络中的二进制网络（Binary Neural Network）或量化权重的位宽统计中，这是基础算子。"},
                    {"id": "190", "name": "Reverse Bits", "difficulty": "Easy", "key": "逐位移位逆转", "systems_note": "在网络数据包大端序与小端序（Big-endian / Little-endian）转换、或图像底层像素位对齐中，需要将二进制位完全倒置，考察了位运算的基本操作。"},
                    {"id": "137", "name": "Single Number II", "difficulty": "Medium", "key": "二进制各数位求余累加 / 逻辑门电路模拟", "systems_note": "在 ML 硬件级加速芯片（如 ASIC、FPGA）或 SIMD 指令集优化中，模拟逻辑电路中的状态机转换来对任意 k 周期重复数据进行过滤，是极具代表性的硬件联想题。"}
                ]
            },
            21: {
                "theme": "缓存算法手撕实战 (Cache System Implementation)",
                "problems": [
                    {"id": "146", "name": "LRU Cache", "difficulty": "Medium", "key": "哈希表 + 双向循环链表 (O(1) 实战)", "systems_note": "MLSys 中的核心考点。大模型推理中的 KV Cache 换入换出机制、分布式深度学习参数服务器（Parameter Server）中的冷热权重同步，全部依赖于 LRU 缓存架构。必须能熟练、快速地在白板上实现哈希表与双向链表的就地解耦与重连操作，保证查询和插入均为 O(1)。在面试中，常被追问如何通过读写锁（`shared_mutex`）或细粒度锁使其实现并发安全。"},
                    {"id": "460", "name": "LFU Cache", "difficulty": "Hard", "key": "双哈希表 + 频数链表组织", "systems_note": "最难的系统级缓存设计题。当空间已满且存在频数冲突时，需淘汰最久未访问（LRU）的节点。需要维护一个 `min_freq` 变量和 {频数: 该频数对应的双向链表} 的哈希表，是极致的数据结构组装挑战。"},
                    {"id": "622", "name": "Design Circular Queue", "difficulty": "Medium", "key": "数组环形缓冲区边界指针", "systems_note": "环形缓冲区（Ring Buffer）是操作系统进程间通信（IPC）、生产者-消费者管道、以及 GPU 命令队列（Command Queue）中的核心数据结构。通过 `(tail + 1) % size` 来管理循环写入，实现无锁并发数据交换的基础模型。"}
                ]
            }
        }
    },
    {
        "name": "Phase 4: 动态规划与全真高压模拟 (Day 22-30)",
        "target": "掌握一维/二维 DP 状态转移推导，学会使用剪枝与空间压缩，并在限时高压模拟下克服盲目卡壳。",
        "days": {
            22: {
                "theme": "一维动态规划与拆分决策 (1D DP)",
                "problems": [
                    {"id": "70", "name": "Climbing Stairs", "difficulty": "Easy", "key": "一维递推 / 滚动变量状态压缩", "systems_note": "动态规划的最简代表。要理解为什么可以用滚动变量（a, b = b, a + b）将空间复杂度从 O(N) 压缩至 O(1)。空间压缩是 MLSys 对海量 Tensor 显存优化的核心追求。"},
                    {"id": "746", "name": "Min Cost Climbing Stairs", "difficulty": "Easy", "key": "带权值的一维递推", "systems_note": "递推公式 `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`。同样可进行空间压缩优化，是建立 DP 状态转移肌肉记忆的基础。"},
                    {"id": "322", "name": "Coin Change", "difficulty": "Medium", "key": "完全背包问题自底向上迭代", "systems_note": "无法使用贪心策略求解的最优组合问题。状态转移方程 `dp[i] = min(dp[i], dp[i - coin] + 1)`，初始化为无穷大。在计算资源分配优化中，这种背包分配模型极为常见。"}
                ]
            },
            23: {
                "theme": "子序列与背包模型 (Sequence & Knapsack DP)",
                "problems": [
                    {"id": "300", "name": "Longest Increasing Subsequence", "difficulty": "Medium", "key": " 耐心理牌二分贪心优化 (O(N log N))", "systems_note": "最优解是利用辅助数组和二分查找在 O(N log N) 内解决。在编译器做指令流水线优化（Instruction Pipeline - 决定哪些不依赖的指令可以并行发射）中，寻找最长单调序列可以为指令重排提供直接依据。"},
                    {"id": "139", "name": "Word Break", "difficulty": "Medium", "key": "前缀切分 DP + 字典 Set 高速查找", "systems_note": "判断一段连续流是否可以被有效切分。状态转移为 `dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`。在 NLP 分词及算子大图切分生成中，这种前缀切分逻辑扮演重要角色。"},
                    {"id": "416", "name": "Partition Equal Subset Sum", "difficulty": "Medium", "key": "0-1 背包问题状态压缩", "systems_note": "典型的 0-1 背包。为了防止空间溢出，我们需要使用从右往左的一维 DP 倒序更新，将空间复杂度降到 O(target)。在分布式计算中，任务划分以实现负载均衡通常可退化为此类背包分割。"}
                ]
            },
            24: {
                "theme": "二维动态规划与网格状态 (2D DP)",
                "problems": [
                    {"id": "62", "name": "Unique Paths", "difficulty": "Medium", "key": "二维网格自上自左累加 / 一维行滚动压缩", "systems_note": "经典的网格路线规划。状态转移 `dp[i][j] = dp[i-1][j] + dp[i][j-1]`。在物理芯片的二维网格布线（NoC - Network on Chip 芯片上路由器数据路由设计）中，分析路由包的流动路径概率与此模型高度重合。可做一维行空间压缩。"},
                    {"id": "1143", "name": "Longest Common Subsequence", "difficulty": "Medium", "key": "二维子序列比对矩阵", "systems_note": "在比较两个大规模神经网络结构差异（或两份编译代码相似度 Diff 工具）时，LCS 是核心底层比对算法。时间复杂度为 O(M*N)，通常会涉及空间维度的滚动压缩面试追问。"},
                    {"id": "72", "name": "Edit Distance", "difficulty": "Hard", "key": "二维操作决策 (插入、删除、替换)", "systems_note": "字符编辑的最佳路径代价计算。通过分析三种状态来源 `dp[i-1][j]`、`dp[i][j-1]` 和 `dp[i-1][j-1]` 构造全局转移网格。是高阶 DP 状态分析功底的试金石。"}
                ]
            },
            25: {
                "theme": "区间与树形动态规划 (Interval & Tree DP)",
                "problems": [
                    {"id": "96", "name": "Unique Binary Search Trees", "difficulty": "Medium", "key": "卡特兰数 (Catalan Number) 递推", "systems_note": "统计所有可能生成的 BST 数量。通过累加左子树可能数与右子树可能数的乘积，推导出递推关系式。展示了状态划分的数学对称性。"},
                    {"id": "337", "name": "House Robber III", "difficulty": "Medium", "key": "树形 DP + 节点状态元组传递", "systems_note": "在计算图（Computational Graph）的算子融合选择中，如果相邻的算子不能同时参与某种全局优化，那么最大优化收益的计算就是典型的树形 DP。DFS 返回 `(抢当前节点的最大值, 不抢当前节点的最大值)` 的元组，将复杂度限制在完美的 O(N)。"},
                    {"id": "312", "name": "Burst Balloons", "difficulty": "Hard", "key": "区间 DP / 自底向上填表", "systems_note": "区间 DP 巅峰。通过逆向思考“哪一个气球是最后一个被戳破的”，将大区间分割为两个独立子区间加额外收益，从而写出状态转移方程。主要在复杂的算子串联调度优化中作为数学底座。"}
                ]
            },
            26: {
                "theme": "贪心决策与区间调度 (Greedy Algorithms)",
                "problems": [
                    {"id": "55", "name": "Jump Game", "difficulty": "Medium", "key": "贪心策略 - 自后向前更新 goal", "systems_note": "在资源管理中判定任务能否在一系列具有最大跳转能力的节点间安全传递。自后向前维护当前的“最前可达点” goal，时间复杂度 O(N)，空间复杂度 O(1)，大幅优于一维 DP 的 O(N^2) 方案。"},
                    {"id": "134", "name": "Gas Station", "difficulty": "Medium", "key": "总余量判定 + 起点自前向后移位", "systems_note": "如果总加油量大于总消耗量，必然有解。通过一次遍历，一旦当前油量归负就将起点设为下一站，巧妙地将 O(N^2) 查找降至 O(N) 贪心决策。"},
                    {"id": "406", "name": "Queue Reconstruction by Height", "difficulty": "Medium", "key": "排序 + 贪心插入位置", "systems_note": "在多资源争抢的优先级队列调度中，根据两个维度的权重动态安排优先级。通过先降序排高度、再按 K 索引插入的方法，实现了局部的最优队列重构。"}
                ]
            },
            27: {
                "theme": "区间重叠与多维度调度 (Intervals & Scheduling)",
                "problems": [
                    {"id": "56", "name": "Merge Intervals", "difficulty": "Medium", "key": "起点排序 + 顺序区间合并", "systems_note": "在操作系统的物理内存分配器中，当多个虚拟页面被释放时，我们需要将相邻且相接的空闲内存区间进行“物理合并”，以减少系统内存碎片。这个合并的核心逻辑就是区间合并。"},
                    {"id": "435", "name": "Non-overlapping Intervals", "difficulty": "Medium", "key": "贪心策略 - 终点排序优先保留先结束区间", "systems_note": "经典的区间调度问题。为了给后面留出尽可能多的调度空间，应当优先保留结束时间最早的区间。常用于高并发事件调度器和算子流水线调度中。"},
                    {"id": "621", "name": "Task Scheduler", "difficulty": "Medium", "key": "桶模型贪心 / 冷却时间公式计算", "systems_note": "在操作系统的 CPU 核心任务调度或 GPU 算子多通道流水发射中，相同类型的任务必须间隔一定的 Cooldown 冷却时间才能再次发射。通过统计最高频任务填充桶的方法，可实现在 O(N) 时间内计算出最小执行总周期。"}
                ]
            },
            28: {
                "theme": "全真高压模拟 Day 1 (Google/Meta 偏底层高频真题)",
                "problems": [
                    {"id": "307", "name": "Range Sum Query 2D - Mutable", "difficulty": "Hard", "key": "树状数组 (Binary Indexed Tree / Fenwick Tree) / 线段树", "systems_note": "在动态 ML 算子中，当局部权重频繁被修改（Mutable），且同时需要频繁查询区域总和时，普通前缀和会导致修改代价高达 O(N)。使用树状数组，可使得单点更新和区域查询的复杂度均为完美的 O(log N)，体现了高级系统的折中优化。"},
                    {"id": "588", "name": "Design In-Memory File System", "difficulty": "Hard", "key": "Trie 树扩展节点设计 + 目录树 DFS", "systems_note": "手撕内存文件系统。核心是设计一个包含 {子目录名: 节点} 且叶子节点能存储具体文件内容的 Trie 树，支持 `ls`, `mkdir`, `addContentToFile`, `readContentFromFile` 等操作。考查了高并发操作系统底层模拟构建。"}
                ]
            },
            29: {
                "theme": "全真高压模拟 Day 2 (NVIDIA/Apple 硬件与并发关联真题)",
                "problems": [
                    {"id": "311", "name": "Sparse Matrix Multiplication", "difficulty": "Medium", "key": "稀疏表示行主序非零遍历优化 (CRS / CSR 压缩格式)", "systems_note": "深度学习中稀疏神经网络（Sparse Neural Network）计算的绝对核心。在 GPU 计算中，如果直接对大量为 0 的节点做密集乘法会极度浪费带宽和算力。使用行主序只对非零节点进行累加运算，极大地模拟了 CSR 格式的硬件加速逻辑。"},
                    {"id": "380", "name": "Insert Delete GetRandom O(1)", "difficulty": "Medium", "key": "哈希表 + 动态数组交换尾部元素删除", "systems_note": "很多 MLSys 的负采样（Negative Sampling）中需要在 O(1) 内随机抽取样本，同时支持 O(1) 的插入和删除。哈希表做映射，数组存储实际元素。删除时将目标与数组尾部元素交换再 pop_back，避免了数组搬移开销。"}
                ]
            },
            30: {
                "theme": "全真高压模拟 Day 3 (大厂 Hard 极客挑战终局模拟)",
                "problems": [
                    {"id": "460", "name": "LFU Cache", "difficulty": "Hard", "key": "手撕 LFU (复习 Day 21)", "systems_note": "在高并发网关及存储引擎底层，淘汰频率最低的缓存节点。在高压限时下，必须做到双哈希表和双向链表操作行云流水无 Bug。"},
                    {"id": "212", "name": "Word Search II", "difficulty": "Hard", "key": "手撕 Trie + Grid DFS (复习 Day 14)", "systems_note": "综合考察前缀树、矩阵 DFS、回溯算法和叶子树枝剪枝优化，是考察复杂路径探索的压轴题。"},
                    {"id": "269", "name": "Alien Dictionary", "difficulty": "Hard", "key": "手撕拓扑排序有向图环检测 (复习 Day 16)", "systems_note": "系统编译调度的基石，将输入依赖解析、建图、环检测、拓扑排序汇于一体，极其考验白板代码的完整度和鲁棒性。"}
                ]
            }
        }
    }
]
