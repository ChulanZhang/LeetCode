# LeetCode Python 3 面试语法与常用标准库终极指南

本指南专为算法面试设计，涵盖了 LeetCode 刷题和面试白板写代码时最常用、最高效的 Python 3 语法、内置数据结构、标准库及避坑指南。

---

## 一、 核心数据结构与内置 Collections

### 1. 列表 (List) 与切片 (Slicing)
列表是 Python 中最基本也是最灵活的数据结构，支持动态扩容。

- **切片语法**：`list[start:end:step]`（左闭右开）
  ```python
  arr = [0, 1, 2, 3, 4, 5]
  arr[1:4]      # [1, 2, 3] (步长默认为 1)
  arr[::-1]     # [5, 4, 3, 2, 1, 0] (原地翻转的快速拷贝表示)
  arr[::2]      # [0, 2, 4] (偶数索引元素)
  arr[1:4:2]    # [1, 3]
  ```
- **列表生成式 (List Comprehension)**：
  ```python
  # 生成二维网格 dp[m][n] 初始化为 0 (千万不要用 [[0]*n]*m，这会导致行共享同一片物理内存！)
  dp = [[0] * n for _ in range(m)]
  
  # 过滤生成
  evens = [x for x in range(10) if x % 2 == 0]
  ```
- **高效删除/插入**：
  - `pop()`: 弹出末尾元素，时间复杂度 $O(1)$。
  - `pop(0)` / `insert(0, val)`: 头部弹出/插入，时间复杂度 $O(N)$。**若需要频繁在首尾进行操作，必须使用 `deque`。**

### 2. 双端队列 (collections.deque)
在 BFS（广度优先搜索）和滑动窗口最大值（单调队列）中，`deque` 是绝对的核心。

- **底层结构**：双向链表，在两端插入/删除时间复杂度为绝对的 $O(1)$。
- **核心操作**：
  ```python
  from collections import deque
  
  q = deque([1, 2, 3])
  q.append(4)         # 右侧入队 -> [1, 2, 3, 4]
  q.appendleft(0)     # 左侧入队 -> [0, 1, 2, 3, 4]
  q.pop()             # 右侧出队 -> 返回 4，队列变为 [0, 1, 2, 3]
  q.popleft()         # 左侧出队 -> 返回 0，队列变为 [1, 2, 3]
  ```

### 3. 哈希表与计数器 (dict & defaultdict & Counter)
在频数统计、两数之和、无重复子串等问题中频繁使用。

- **默认值哈希表 (defaultdict)**：避免繁琐的 `if key not in d` 判断。
  ```python
  from collections import defaultdict
  
  # 自动初始化为空列表
  adj = defaultdict(list)
  adj[1].append(2)  # 无需先判断 1 是否在字典中
  
  # 自动初始化为整数 0，适用于频数统计
  counts = defaultdict(int)
  counts['a'] += 1
  
  # 自动初始化为集合 set
  visited = defaultdict(set)
  visited['user1'].add('page_a')
  ```
- **频数统计计数器 (Counter)**：
  ```python
  from collections import Counter
  
  counts = Counter("abcaba")  # Counter({'a': 3, 'b': 2, 'c': 1})
  
  # 获取频率最高的 K 个元素 (返回格式: [(元素, 频数), ...])
  top_k = counts.most_common(2)  # [('a', 3), ('b', 2)]
  
  # 两个计数器直接做差（仅保留正频数），或求交集/并集
  c1 = Counter(a=2, b=1)
  c2 = Counter(a=1, b=2)
  diff = c1 - c2  # Counter({'a': 1})
  ```

### 4. 哈希集合 (set)
支持 $O(1)$ 的成员判定、去重及集合运算。

- **核心操作**：
  ```python
  s = set([1, 2, 3])
  s.add(4)
  s.remove(4)      # 若元素不存在，会抛出 KeyError
  s.discard(4)     # 若元素不存在，安全退出不报错 (面试推荐！)
  
  # 集合运算
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  union = s1 | s2          # {1, 2, 3, 4, 5} (并集)
  intersect = s1 & s2      # {3} (交集)
  diff = s1 - s2           # {1, 2} (差集)
  ```

---

## 二、 排序与自定义比较器

Python 3 移除了 `cmp` 参数，改用 `key` 函数结合 `lambda` 或 `cmp_to_key` 进行排序。

### 1. 基础多维度排序
默认 `sort()` 和 `sorted()` 是稳定排序。元组升序排序时，会先对比第一个元素，相等时再对比第二个元素，依此类推。
```python
# 按照元素的绝对值排序
arr = [-3, 1, -2, 4]
arr.sort(key=abs)  # [1, -2, -3, 4]

# 多维度排序：先按第一维度升序，若第一维度相等，按第二维度降序
# 技巧：如果是数字，降序可以用负号 '-' 实现
intervals = [[1, 4], [2, 3], [1, 5]]
intervals.sort(key=lambda x: (x[0], -x[1]))
# 结果: [[1, 5], [1, 4], [2, 3]]
```

### 2. 高级自定义排序 (`cmp_to_key`)
对于不能直接加负号的非数值类型（如字符串拼接对比，例如 LeetCode 179 最大数），需使用 `functools.cmp_to_key`。
```python
from functools import cmp_to_key

def compare(x, y):
    # 拼接字符串后对比大小
    if x + y > y + x:
        return -1  # x 应该排在 y 前面 (在 Python 中返回负数代表 x 小，排在前面)
    elif x + y < y + x:
        return 1
    else:
        return 0

nums = ["3", "30", "34", "5", "9"]
nums.sort(key=cmp_to_key(compare))
# 结果: ['9', '5', '34', '3', '30']
```

---

## 三、 堆与优先队列 (heapq)

Python 的 `heapq` 库仅支持 **最小堆 (Min-Heap)**。若需最大堆，需要将元素**取反/负数化**存入。

### 1. 基础操作
```python
import heapq

heap = []
# 1. 插入元素
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

# 2. 弹出堆顶（最小元素）
min_val = heapq.heappop(heap)  # 返回 1，此时 heap 变为 [3, 4]

# 3. 查看堆顶（不弹出）
peek_val = heap[0]  # 返回 3

# 4. 原地建堆：将一个无序列表在 O(N) 时间内转换为最小堆
nums = [5, 1, 9, 3]
heapq.heapify(nums)  # nums 原地变更为堆结构
```

### 2. 最大堆 (Max-Heap) 实现
```python
# 存储负数以模拟最大堆
max_heap = []
nums = [5, 1, 9, 3]
for num in nums:
    heapq.heappush(max_heap, -num)

# 弹出最大值（取出时需取反恢复）
max_val = -heapq.heappop(max_heap)  # 返回 9
```

### 3. 多维度/自定义对象存入堆
在 `heapq` 中，如果存入的是元组 `(priority, item)`，堆会首先比较 `priority`。如果 `priority` 相等，它会继续比较 `item`。
**避坑指南**：如果 `item` 是自定义的对象（如二叉树的 `TreeNode`），由于 `TreeNode` 没有定义 `<` 运算符，如果 `priority` 冲突，Python 会抛出比较报错。
- **解决方法**：存入三元组 `(priority, count, item)`。`count` 是一个单调递增的整数，用于在优先级相等时进行唯一打破，防止比较 `item` 本身。
  ```python
  import heapq
  
  heap = []
  counter = 0
  
  # 压入二叉树节点，使用 counter 避开 TreeNode 的直接比较
  heapq.heappush(heap, (node1.val, counter, node1))
  counter += 1
  ```

---

## 四、 二分查找标准库 (bisect)

面试中直接手写二分查找容易发生越界或边界死循环，Python 提供了非常稳健的内置二分搜索库。

```python
import bisect

arr = [1, 3, 3, 6, 8, 10]

# 1. bisect_left(arr, x)：寻找插入点，如果有相等元素，插入在左侧（即返回第一个 >= x 的元素索引）
idx_left = bisect.bisect_left(arr, 3)   # 返回 1
idx_left_none = bisect.bisect_left(arr, 5) # 返回 3 (6 的索引)

# 2. bisect_right(arr, x)：寻找插入点，如果有相等元素，插入在右侧（即返回第一个 > x 的元素索引）
idx_right = bisect.bisect_right(arr, 3) # 返回 3 (6 的索引)
```

### 🎯 二分库实战配方
- **寻找第一个 `>= target` 的元素**：`idx = bisect.bisect_left(arr, target)`。若 `idx < len(arr)` 且 `arr[idx] == target`，则找到了该值；若不等于，则 `idx` 处是第一个大于该值的元素。
- **寻找最后一个 `<= target` 的元素**：`idx = bisect.bisect_right(arr, target) - 1`。若 `idx >= 0`，则 `arr[idx]` 即为所求。

---

## 五、 数学与位运算

### 1. 极限值表示
LeetCode 中常需要初始化最大/最小值。
```python
import math

max_val = float('inf')      # 正无穷大
min_val = float('-inf')     # 负无穷大

# 也可以使用 math 库的常数 (Python 3.5+)
max_val = math.inf
min_val = -math.inf
```

### 2. 整数除法与余数
```python
# 1. 地板除 (向下取整)
5 // 2   # 2
-5 // 2  # -3 (避坑：负数地板除是向更小的负数取整！)

# 2. 截断除法 (向 0 取整 - 面试最常用)
int(-5 / 2) # -2

# 3. 最大公约数 (GCD)
math.gcd(12, 8)  # 返回 4
```

### 3. 高频位运算
- **异或操作**：`a ^ b`
- **移位操作**：`n >> 1`（相当于除以 2 并向下取整），`n << 1`（相当于乘以 2）。
- **判定奇偶**：`n & 1 == 1`（奇数），`n & 1 == 0`（偶数）。
- **消除二进制最低位的 1**：`n & (n - 1)`（可用于快速统计 1 的个数，即 Hamming Weight，或判定是否为 2 的幂次）。
- **获取最低位的 1（Lowbit）**：`n & -n`（树状数组的核心）。

---

## 六、 记忆化递归与动态规划助手 (functools)

对于基于 DFS/递归的记忆化搜索（Memoization），不需要再手动声明全局或传入 `memo` 哈希表，直接使用 `@cache` 装饰器。

```python
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

- **底层机制**：自动将函数的 `(arguments)` 作为 Key，返回值作为 Value 存入内置哈希表中。再次调用时直接 $O(1)$ 返回。
- **向下兼容版本**：若 Python 版本较低，可使用 `@lru_cache(None)`，其效果与 `@cache` 完全等价且不限制缓存容量。
  ```python
  from functools import lru_cache
  
  @lru_cache(None)
  def dfs(state):
      # 带记忆化的深度优先搜索
      pass
  ```

---

## 七、 栈深度与编译器深度设置 (sys)

如果在树的 DFS 或常规递归中遇到了退化树（高度达到 $10^4$ 级别），Python 的默认递归深度限制（通常是 1000）会导致抛出 `RecursionError`。
```python
import sys

# 在代码头部将最大递归调用深度设置为十万（防止深度 DFS 栈溢出）
sys.setrecursionlimit(100000)
```

---

## 八、 常见内置工具函数

### 1. `enumerate` (获取索引与值)
```python
for idx, num in enumerate(nums):
    print(f"Index: {idx}, Value: {num}")
```

### 2. `zip` (并行打包遍历)
```python
names = ["Alice", "Bob"]
scores = [95, 88]

# 遍历打包
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 二维矩阵旋转转置的骚操作 (Zip 拆包)
matrix = [[1, 2], [3, 4]]
transposed = list(zip(*matrix))  # [(1, 3), (2, 4)]
```

### 3. `reversed` 与 `reverse()`
- `arr.reverse()`: **原地**修改列表，无返回值。
- `reversed(arr)`: 返回一个**逆序迭代器**，不改变原列表，适合在 `for` 循环中逆序遍历。
  ```python
  for x in reversed([1, 2, 3]):
      # 依次输出 3, 2, 1
  ```
