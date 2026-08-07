# Ultimate Guide to Python 3 for LeetCode & Coding Interviews

This guide is designed for algorithm interviews, covering the most common, efficient Python 3 syntax, built-in data structures, standard libraries, and common pitfalls to avoid when coding on LeetCode or a whiteboard.

---

## 1. Core Data Structures & Built-in Collections

### 1.1 List & Slicing
Lists are the most basic and flexible dynamic array implementations in Python.

- **Slicing Syntax**: `list[start:end:step]` (left-closed, right-open)
  ```python
  arr = [0, 1, 2, 3, 4, 5]
  arr[1:4]      # [1, 2, 3] (default step is 1)
  arr[::-1]     # [5, 4, 3, 2, 1, 0] (fast shallow copy reversed)
  arr[::2]      # [0, 2, 4] (even index elements)
  arr[1:4:2]    # [1, 3]
  ```
- **List Comprehensions**:
  ```python
  # Initializing a 2D grid dp[m][n] to 0
  # Avoid using [[0]*n]*m because it makes all rows share the same physical memory reference!
  dp = [[0] * n for _ in range(m)]
  
  # List filtering
  evens = [x for x in range(10) if x % 2 == 0]
  ```
- **Efficient Deletions/Insertions**:
  - `pop()`: Pops the last element, O(1) time complexity.
  - `pop(0)` / `insert(0, val)`: Pops/inserts at the head, O(N) time complexity. **If you need frequent operations at both ends, you must use a `deque`.**

### 1.2 Double-Ended Queue (collections.deque)
`deque` is the default structure for Breadth-First Search (BFS) and sliding window maximums (monotonic queues).

- **Underlying structure**: Doubly linked list, providing O(1) insertion/deletion at both ends.
- **Core Operations**:
  ```python
  from collections import deque
  
  q = deque([1, 2, 3])
  q.append(4)         # Push to right -> [1, 2, 3, 4]
  q.appendleft(0)     # Push to left -> [0, 1, 2, 3, 4]
  q.pop()             # Pop from right -> returns 4, queue becomes [0, 1, 2, 3]
  q.popleft()         # Pop from left -> returns 0, queue becomes [1, 2, 3]
  ```

### 1.3 Hash Maps & Counters (dict, defaultdict, Counter)
Widely used for frequency counting, hash-based lookups, and tracking visited items.

- **defaultdict**: Avoids verbose `if key not in d` checks by initializing keys with a default factory.
  ```python
  from collections import defaultdict
  
  # Automatically initialize to an empty list
  adj = defaultdict(list)
  adj[1].append(2)  # No need to check if 1 is in the dict first
  
  # Automatically initialize to 0 (ideal for count accumulation)
  counts = defaultdict(int)
  counts['a'] += 1
  
  # Automatically initialize to an empty set
  visited = defaultdict(set)
  visited['user1'].add('page_a')
  ```
- **Counter**: High-level utility for tracking occurrences.
  ```python
  from collections import Counter
  
  counts = Counter("abcaba")  # Counter({'a': 3, 'b': 2, 'c': 1})
  
  # Get top K most frequent elements (returns list of tuples: [(element, frequency), ...])
  top_k = counts.most_common(2)  # [('a', 3), ('b', 2)]
  
  # Arithmetic operations between counters (keeps positive frequencies only)
  c1 = Counter(a=2, b=1)
  c2 = Counter(a=1, b=2)
  diff = c1 - c2  # Counter({'a': 1})
  ```

### 1.4 Hash Set (set)
Provides O(1) membership testing, deduplication, and mathematical set operations.

- **Core Operations**:
  ```python
  s = set([1, 2, 3])
  s.add(4)
  s.remove(4)      # Raises KeyError if 4 does not exist
  s.discard(4)     # Safe remove: exits silently if 4 does not exist (recommended for interviews)
  
  # Set operations
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  union = s1 | s2          # {1, 2, 3, 4, 5} (Union)
  intersect = s1 & s2      # {3} (Intersection)
  diff = s1 - s2           # {1, 2} (Difference)
  ```

---

## 2. Sorting & Custom Comparators

Python 3 removed the `cmp` argument from sort functions. Custom sorting is done using the `key` argument combined with lambdas or `cmp_to_key`.

### 2.1 Multi-Key Sorting
Python's built-in `sort()` and `sorted()` are stable. When sorting tuples, elements are compared element-by-element from left to right.
```python
# Sort elements by their absolute values
arr = [-3, 1, -2, 4]
arr.sort(key=abs)  # [1, -2, -3, 4]

# Multi-key sorting: Sort by start time ascending, then by end time descending
# Tip: For numeric values, descending order can be achieved by negating the value
intervals = [[1, 4], [2, 3], [1, 5]]
intervals.sort(key=lambda x: (x[0], -x[1]))
# Result: [[1, 5], [1, 4], [2, 3]]
```

### 2.2 Custom Comparator (`cmp_to_key`)
For non-numeric sorting rules (such as string concatenation comparisons like in LeetCode 179 - Largest Number), use `functools.cmp_to_key`.
```python
from functools import cmp_to_key

def compare(x, y):
    # Compare concatenated strings
    if x + y > y + x:
        return -1  # x should come before y (returns negative in Python)
    elif x + y < y + x:
        return 1
    else:
        return 0

nums = ["3", "30", "34", "5", "9"]
nums.sort(key=cmp_to_key(compare))
# Result: ['9', '5', '34', '3', '30']
```

---

## 3. Heaps & Priority Queues (heapq)

Python's `heapq` module implements **Min-Heaps** by default. To implement a Max-Heap, you must **negate** the values before pushing.

### 3.1 Basic Operations
```python
import heapq

heap = []
# 1. Push an element onto the heap
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

# 2. Pop the smallest element
min_val = heapq.heappop(heap)  # Returns 1, heap becomes [3, 4]

# 3. Peek at the smallest element (without popping)
peek_val = heap[0]  # Returns 3

# 4. Heapify: Transform a list into a min-heap in-place in O(N) time
nums = [5, 1, 9, 3]
heapq.heapify(nums)  # nums becomes a valid min-heap
```

### 3.2 Max-Heap Implementation
```python
# Negate values to simulate a Max-Heap
max_heap = []
nums = [5, 1, 9, 3]
for num in nums:
    heapq.heappush(max_heap, -num)

# Retrieve the maximum value (negate back on pop)
max_val = -heapq.heappop(max_heap)  # Returns 9
```

### 3.3 Custom Object / Multi-Key Heap Storage
If storing tuples like `(priority, item)` in `heapq`, comparisons will fall back to `item` if `priority` matches.
**Common Trap**: If `item` is a custom object without comparison operators defined (like a tree `TreeNode`), Python will throw a type comparison error.
- **Solution**: Store a 3-tuple `(priority, count, item)` where `count` is a monotonically increasing integer that breaks ties uniquely, avoiding comparison of `item` itself.
  ```python
  import heapq
  
  heap = []
  counter = 0
  
  # Push TreeNode, using counter to bypass direct TreeNode comparison on conflict
  heapq.heappush(heap, (node1.val, counter, node1))
  counter += 1
  ```

---

## 4. Binary Search Library (bisect)

To avoid off-by-one errors and infinite loops during binary search implementations, use Python's built-in `bisect` library.

```python
import bisect

arr = [1, 3, 3, 6, 8, 10]

# 1. bisect_left(arr, x): Find insertion index to keep sorted. If x exists, insert before/left (returns index of first element >= x)
idx_left = bisect.bisect_left(arr, 3)   # Returns 1
idx_left_none = bisect.bisect_left(arr, 5) # Returns 3 (index of 6)

# 2. bisect_right(arr, x): Find insertion index to keep sorted. If x exists, insert after/right (returns index of first element > x)
idx_right = bisect.bisect_right(arr, 3) # Returns 3 (index of 6)
```

### 🎯 Binary Search Recipes
- **Find first element `>= target`**: `idx = bisect.bisect_left(arr, target)`. Check if `idx < len(arr)` and `arr[idx] == target` to confirm an exact match.
- **Find last element `<= target`**: `idx = bisect.bisect_right(arr, target) - 1`. If `idx >= 0`, `arr[idx]` is the target.

---

## 5. Math & Bit Manipulation

### 5.1 Infinity Representations
```python
import math

max_val = float('inf')      # Positive infinity
min_val = float('-inf')     # Negative infinity

# Alternately, using the math module
max_val = math.inf
min_val = -math.inf
```

### 5.2 Integer Division & Modulo
```python
# 1. Floor division (rounds down)
5 // 2   # 2
-5 // 2  # -3 (Common Trap: rounds down towards negative infinity!)

# 2. Truncated division (rounds towards zero - standard in C++/Java)
int(-5 / 2) # -2

# 3. Greatest Common Divisor (GCD)
math.gcd(12, 8)  # Returns 4
```

### 5.3 High-Frequency Bit Operations
- **Bitwise XOR**: `a ^ b`
- **Bitwise Shift**: `n >> 1` (divides by 2, rounds down), `n << 1` (multiplies by 2).
- **Parity check**: `n & 1 == 1` (odd), `n & 1 == 0` (even).
- **Clear LSB (Lowest Set Bit)**: `n & (n - 1)` (efficient for counting set bits or checking if `n` is a power of 2).
- **Isolate LSB (Lowest Set Bit)**: `n & -n` (used in Fenwick Trees / Binary Indexed Trees).

---

## 6. Memoization & Dynamic Programming (functools)

For depth-first searches or recursive state lookups, use the `@cache` decorator to avoid manual dictionary hashing.

```python
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

- **Mechanism**: Automatically caches input arguments as hash keys and values as outputs in an internal hash table. Repeated calls are resolved in O(1) time.
- **LRU Cache Alternate**: For older versions of Python or capped cache allocations, use `@lru_cache(None)`, which is equivalent to `@cache`.
  ```python
  from functools import lru_cache
  
  @lru_cache(None)
  def dfs(state):
      # Memoized DFS
      pass
  ```

---

## 7. Recursion Stack Limit (sys)

If traversing deep tree paths or linear graphs, Python's default recursion limit (usually 1000) will throw a `RecursionError`. Increase it in the head of your script.
```python
import sys

# Set maximum recursion depth to 100,000 to prevent stack overflow in deep DFS traversals
sys.setrecursionlimit(100000)
```

---

## 8. Essential Built-in Helpers

### 8.1 `enumerate`
```python
for idx, num in enumerate(nums):
    print(f"Index: {idx}, Value: {num}")
```

### 8.2 `zip`
```python
names = ["Alice", "Bob"]
scores = [95, 88]

# Synchronous unpacking
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Rotate/transpose a 2D matrix
matrix = [[1, 2], [3, 4]]
transposed = list(zip(*matrix))  # [(1, 3), (2, 4)]
```

### 8.3 `reversed` & `reverse()`
- `arr.reverse()`: Mutates the list **in-place**; has no return value.
- `reversed(arr)`: Returns a **reverse iterator**; does not modify the original list.
  ```python
  for x in reversed([1, 2, 3]):
      # Loops through 3, 2, 1
  ```
