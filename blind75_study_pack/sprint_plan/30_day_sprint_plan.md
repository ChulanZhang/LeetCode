# 30-Day Algorithm Sprint Plan (Customized for MLSys PhDs)

> **Coach's Note**: Specially customized for MLSys backgrounds. While strengthening core algorithms like two pointers, binary search, trees, and graphs, we deeply integrate systems-level mechanics (LRU/LFU cache, ring buffers, concurrency, bit quantization) to build high-performance whiteboard muscle memory.

## 30-Day Panorama Roadmap

| Phase | Day | Core Theme | Daily Volume |
|---|---|---|---|
| Phase 1 | Day 01 | Arrays & Two Pointers | 3 Qs |
| Phase 1 | Day 02 | Sliding Window | 3 Qs |
| Phase 1 | Day 03 | Fast & Slow Pointers | 3 Qs |
| Phase 1 | Day 04 | Monotonic Stack | 3 Qs |
| Phase 1 | Day 05 | Monotonic Queue | 2 Qs |
| Phase 1 | Day 06 | Prefix Sums & Difference Arrays | 3 Qs |
| Phase 1 | Day 07 | Matrix Operations & Locality | 3 Qs |
| Phase 2 | Day 08 | Binary Search | 3 Qs |
| Phase 2 | Day 09 | Advanced Binary Search | 3 Qs |
| Phase 2 | Day 10 | Tree Recursion & BFS | 3 Qs |
| Phase 2 | Day 11 | BST & LCA | 3 Qs |
| Phase 2 | Day 12 | Tree Construction & DFS | 3 Qs |
| Phase 2 | Day 13 | Backtracking Basics | 3 Qs |
| Phase 2 | Day 14 | Advanced Backtracking | 2 Qs |
| Phase 3 | Day 15 | Graph Traversals | 3 Qs |
| Phase 3 | Day 16 | Topological Sort & Scheduling | 3 Qs |
| Phase 3 | Day 17 | Union-Find & Equivalence Classes | 3 Qs |
| Phase 3 | Day 18 | Prefix Trees (Trie) | 3 Qs |
| Phase 3 | Day 19 | Heaps & Priority Schedulers | 3 Qs |
| Phase 3 | Day 20 | Bit Manipulation & Lower-Precision Formats | 4 Qs |
| Phase 3 | Day 21 | Cache System Implementation | 3 Qs |
| Phase 4 | Day 22 | 1D Dynamic Programming | 3 Qs |
| Phase 4 | Day 23 | Subsequences & Knapsack DP | 3 Qs |
| Phase 4 | Day 24 | 2D Grid Dynamic Programming | 3 Qs |
| Phase 4 | Day 25 | Interval & Tree DP | 3 Qs |
| Phase 4 | Day 26 | Greedy Algorithms | 3 Qs |
| Phase 4 | Day 27 | Intervals & Scheduling | 3 Qs |
| Phase 4 | Day 28 | Mock Simulator Day 1 (Google/Meta Core Systems) | 2 Qs |
| Phase 4 | Day 29 | Mock Simulator Day 2 (NVIDIA/Apple Hardware & Concurrency) | 2 Qs |
| Phase 4 | Day 30 | Mock Simulator Day 3 (FAANG Hard Graduation Challenges) | 3 Qs |

---

## Phase 1: Foundations & Pointer Intuition (Days 1-7)
**Phase Target**: Master two pointers (left-right, fast-slow), sliding windows, monotonic stacks/queues, and prefix sums. Build strong memory muscle for array/list transformations and eliminate boundary pointer bugs.

### 📅 Day 01 - Arrays & Two Pointers

- **LeetCode 1**: [Two Sum](https://leetcode.com/problems/two-sum/) | **[Easy]**
  - 🔑 **Key Points**: Hash Map / Two Pointers
  - 💻 **Local Template**: [sprint_plan/templates/day01_q001_two_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day01_q001_two_sum.py)
  - 🧠 **MLSys Connection**: Utilizing static hash maps or sorted two-pointer matching is the standard approach for fast table lookups in low-level systems and GPU kernel designs. Optimizing from O(N^2) to O(N) is a classic space-time tradeoff example.

- **LeetCode 15**: [3Sum](https://leetcode.com/problems/3sum/) | **[Medium]**
  - 🔑 **Key Points**: Sorting + Left-Right Pointers
  - 💻 **Local Template**: [sprint_plan/templates/day01_q015_3sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day01_q015_3sum.py)
  - 🧠 **MLSys Connection**: The core of two-pointer searches is search space reduction using monotonicity. Sorting allows us to shift pointers inwards conditionally, pruning the brute-force O(N^3) search space to O(N^2).

- **LeetCode 11**: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | **[Medium]**
  - 🔑 **Key Points**: Two Pointers + Greedy Shifting
  - 💻 **Local Template**: [sprint_plan/templates/day01_q011_container_with_most_water.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day01_q011_container_with_most_water.py)
  - 🧠 **MLSys Connection**: Greedy algorithms are crucial in system scheduling (e.g. choosing nodes with the lowest network latency). Moving the pointer pointing to the shorter line is the only action that can potentially yield a larger area.

---
### 📅 Day 02 - Sliding Window

- **LeetCode 3**: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | **[Medium]**
  - 🔑 **Key Points**: Sliding Window + Hash Set
  - 💻 **Local Template**: [sprint_plan/templates/day02_q003_longest_substring_without_repeating_characters.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day02_q003_longest_substring_without_repeating_characters.py)
  - 🧠 **MLSys Connection**: Sliding window is the standard pattern for contiguous sub-array problems. It is widely used in network protocol layers (e.g. TCP sliding window congestion control) and stream processing systems (e.g. computing average request rates over a sliding temporal window).

- **LeetCode 424**: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | **[Medium]**
  - 🔑 **Key Points**: Sliding Window + Freq Tracking
  - 💻 **Local Template**: [sprint_plan/templates/day02_q424_longest_repeating_character_replacement.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day02_q424_longest_repeating_character_replacement.py)
  - 🧠 **MLSys Connection**: The window condition is that window length L minus the frequency of the most frequent character `max_freq` must be <= k. We maintain a historical `max_freq` to avoid scanning the frequency map of size 26 on every window contraction.

- **LeetCode 76**: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | **[Hard]**
  - 🔑 **Key Points**: Sliding Window + Dual Hash Maps
  - 💻 **Local Template**: [sprint_plan/templates/day02_q076_minimum_window_substring.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day02_q076_minimum_window_substring.py)
  - 🧠 **MLSys Connection**: A benchmark problem for hard sliding windows. In compiler lexical analyzers and low-level pattern scanners, similar sliding window logic is used for high-performance syntax token parsing.

---
### 📅 Day 03 - Fast & Slow Pointers

- **LeetCode 141**: [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | **[Easy]**
  - 🔑 **Key Points**: Floyd's Cycle-Finding Algorithm
  - 💻 **Local Template**: [sprint_plan/templates/day03_q141_linked_list_cycle.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day03_q141_linked_list_cycle.py)
  - 🧠 **MLSys Connection**: Fast and slow pointers are used in OS memory managers to detect if free memory blocks or page descriptors have circular pointer references (which causes memory leak traps or segmentation faults) due to corrupt allocations.

- **LeetCode 142**: [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | **[Medium]**
  - 🔑 **Key Points**: Floyd's Algorithm for Loop Entry
  - 💻 **Local Template**: [sprint_plan/templates/day03_q142_linked_list_cycle_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day03_q142_linked_list_cycle_ii.py)
  - 🧠 **MLSys Connection**: Mathematical proof shows that the distance from the head to the loop entry equals the distance from the pointer meeting point to the loop entry. This demonstrates precise pointer distance manipulation.

- **LeetCode 202**: [Happy Number](https://leetcode.com/problems/happy-number/) | **[Easy]**
  - 🔑 **Key Points**: Implicit Linked List Cycle Detection
  - 💻 **Local Template**: [sprint_plan/templates/day03_q202_happy_number.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day03_q202_happy_number.py)
  - 🧠 **MLSys Connection**: Transformations of a number can be modeled as a directed graph where nodes have out-degree 1 (analogous to a singly linked list). Circular dependency detection can be solved using fast and slow pointers in O(1) auxiliary space.

---
### 📅 Day 04 - Monotonic Stack

- **LeetCode 496**: [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | **[Easy]**
  - 🔑 **Key Points**: Monotonic Decreasing Stack
  - 💻 **Local Template**: [sprint_plan/templates/day04_q496_next_greater_element_i.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day04_q496_next_greater_element_i.py)
  - 🧠 **MLSys Connection**: Monotonic stacks are optimal for 'finding the next greater element'. By maintaining stack monotonicity, we guarantee each element is pushed and popped at most once, achieving a linear O(N) time complexity.

- **LeetCode 739**: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | **[Medium]**
  - 🔑 **Key Points**: Monotonic Stack Storing Indices
  - 💻 **Local Template**: [sprint_plan/templates/day04_q739_daily_temperatures.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day04_q739_daily_temperatures.py)
  - 🧠 **MLSys Connection**: In time-series analysis and system latency metric telemetry (e.g. finding the next timestamp where queue latency drops below a threshold), monotonic stack-based index tracking is a fundamental building block.

- **LeetCode 84**: [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | **[Hard]**
  - 🔑 **Key Points**: Monotonic Increasing Stack + Sentinels
  - 💻 **Local Template**: [sprint_plan/templates/day04_q084_largest_rectangle_in_histogram.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day04_q084_largest_rectangle_in_histogram.py)
  - 🧠 **MLSys Connection**: Used in memory defragmentation (e.g. finding the largest contiguous blocks of physical memory pages). The algorithm calculates areas from the popped taller blocks in O(N) time.

---
### 📅 Day 05 - Monotonic Queue

- **LeetCode 239**: [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | **[Hard]**
  - 🔑 **Key Points**: Monotonic Queue (Double-Ended Queue)
  - 💻 **Local Template**: [sprint_plan/templates/day05_q239_sliding_window_maximum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day05_q239_sliding_window_maximum.py)
  - 🧠 **MLSys Connection**: In MLSys inference servers, we must compute sliding window metrics such as peak inference latency or throughput. Using a double-ended queue (deque) to maintain monotonicity ensures O(N) time complexity for real-time monitoring statistics.

- **LeetCode 862**: [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | **[Hard]**
  - 🔑 **Key Points**: Prefix Sum + Monotonic Deque
  - 💻 **Local Template**: [sprint_plan/templates/day05_q862_shortest_subarray_with_sum_at_least_k.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day05_q862_shortest_subarray_with_sum_at_least_k.py)
  - 🧠 **MLSys Connection**: Finding the shortest subarray satisfying an accumulation threshold in data streams containing negative values. Combining prefix sums with a monotonic deque achieves O(N) optimal search time.

---
### 📅 Day 06 - Prefix Sums & Difference Arrays

- **LeetCode 304**: [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | **[Medium]**
  - 🔑 **Key Points**: 2D Prefix Sums / Integral Image
  - 💻 **Local Template**: [sprint_plan/templates/day06_q304_range_sum_query_2d___immutable.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day06_q304_range_sum_query_2d___immutable.py)
  - 🧠 **MLSys Connection**: A 2D prefix sum is mathematically identical to an 'Integral Image' in computer vision. In CNN (Convolutional Neural Networks) pooling layers or local sum kernels, it optimizes range sum calculations from O(H*W) to O(1).

- **LeetCode 1109**: [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) | **[Medium]**
  - 🔑 **Key Points**: 1D Difference Array
  - 💻 **Local Template**: [sprint_plan/templates/day06_q1109_corporate_flight_bookings.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day06_q1109_corporate_flight_bookings.py)
  - 🧠 **MLSys Connection**: Difference arrays are used to handle batch range addition/subtraction. In task scheduling, if we need to allocate resources over a time window, difference arrays allow O(1) updates per request and reconstruction in O(N) time via prefix sums.

- **LeetCode 1094**: [Car Pooling](https://leetcode.com/problems/car-pooling/) | **[Medium]**
  - 🔑 **Key Points**: Difference Array Overload Checks
  - 💻 **Local Template**: [sprint_plan/templates/day06_q1094_car_pooling.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day06_q1094_car_pooling.py)
  - 🧠 **MLSys Connection**: Used in distributed system concurrency throttling and dynamic GPU memory budget tracking. We convert intervals of resource demands into difference arrays to verify if peak load violates hard hardware capacity constraints.

---
### 📅 Day 07 - Matrix Operations & Locality

- **LeetCode 48**: [Rotate Image](https://leetcode.com/problems/rotate-image/) | **[Medium]**
  - 🔑 **Key Points**: In-Place Transpose + Reflection
  - 💻 **Local Template**: [sprint_plan/templates/day07_q048_rotate_image.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day07_q048_rotate_image.py)
  - 🧠 **MLSys Connection**: Matrix transpose and reflection inspect Cache Locality. In MLSys, tensor dimensions permutes (Transpose/Permute) are extremely common. Fast strided addressing and in-place swapping on contiguous 1D memory buffers are central to GPU kernel optimization.

- **LeetCode 54**: [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | **[Medium]**
  - 🔑 **Key Points**: Boundary Pointer Shrinking Simulation
  - 💻 **Local Template**: [sprint_plan/templates/day07_q054_spiral_matrix.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day07_q054_spiral_matrix.py)
  - 🧠 **MLSys Connection**: Clockwise spiral traversal. It requires strict boundary checks (top, bottom, left, right) to prevent out-of-bounds access, testing precision in array slicing and boundary control.

- **LeetCode 73**: [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | **[Medium]**
  - 🔑 **Key Points**: Row/Column Projection Markers
  - 💻 **Local Template**: [sprint_plan/templates/day07_q073_set_matrix_zeroes.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day07_q073_set_matrix_zeroes.py)
  - 🧠 **MLSys Connection**: An in-place marking scheme when memory is extremely constrained. By projecting zero states onto the first row and first column of the matrix, we achieve O(1) auxiliary space, which is highly practical in embedded or edge computing kernels.

---
## Phase 2: Trees & Binary Search (Days 8-14)
**Phase Target**: Avoid infinite loops in binary search boundary updates, master recursive derivations of tree/BST structures, and build confidence in backtracking and state space pruning.

### 📅 Day 08 - Binary Search

- **LeetCode 704**: [Binary Search](https://leetcode.com/problems/binary-search/) | **[Easy]**
  - 🔑 **Key Points**: Standard Binary Search Template
  - 💻 **Local Template**: [sprint_plan/templates/day08_q704_binary_search.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day08_q704_binary_search.py)
  - 🧠 **MLSys Connection**: The essence of binary search is partition boundary definition and loop condition control. In low-level systems, such as OS memory page table lookup or indexing in sorted key-value databases, binary search is the default O(log N) lookup algorithm.

- **LeetCode 33**: [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | **[Medium]**
  - 🔑 **Key Points**: Monotonic Half Partitioning
  - 💻 **Local Template**: [sprint_plan/templates/day08_q033_search_in_rotated_sorted_array.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day08_q033_search_in_rotated_sorted_array.py)
  - 🧠 **MLSys Connection**: Search in rotated arrays. If split in half, at least one half of the rotated sorted array is guaranteed to be strictly sorted. Detecting which half is sorted allows us to halve the search space at each step.

- **LeetCode 153**: [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | **[Medium]**
  - 🔑 **Key Points**: Inflection Point Binary Search
  - 💻 **Local Template**: [sprint_plan/templates/day08_q153_find_minimum_in_rotated_sorted_array.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day08_q153_find_minimum_in_rotated_sorted_array.py)
  - 🧠 **MLSys Connection**: Compare `mid` with the right boundary `right`. If `nums[mid] > nums[right]`, the inflection point is in the right half, otherwise in the left. This tests the ability to leverage monotonicity in non-trivially sorted sequences.

---
### 📅 Day 09 - Advanced Binary Search

- **LeetCode 74**: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | **[Medium]**
  - 🔑 **Key Points**: Matrix 1D Flat Indexing
  - 💻 **Local Template**: [sprint_plan/templates/day09_q074_search_a_2d_matrix.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day09_q074_search_a_2d_matrix.py)
  - 🧠 **MLSys Connection**: A row-major sorted matrix is stored contiguously in memory as a 1D array. By mapping indices via `(row, col) = (mid // n, mid % n)`, we run standard binary search directly on the flat memory block, avoiding conversion overhead.

- **LeetCode 162**: [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | **[Medium]**
  - 🔑 **Key Points**: Hill Climbing Binary Search
  - 💻 **Local Template**: [sprint_plan/templates/day09_q162_find_peak_element.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day09_q162_find_peak_element.py)
  - 🧠 **MLSys Connection**: In optimization theory and adaptive parameter tuning, 'Hill Climbing' is the fundamental local search heuristic. If the slope at `mid` is ascending, the peak must lie to the right, which guarantees locating a peak in O(log N) time.

- **LeetCode 4**: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | **[Hard]**
  - 🔑 **Key Points**: Binary Search on Array Partitioning
  - 💻 **Local Template**: [sprint_plan/templates/day09_q004_median_of_two_sorted_arrays.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day09_q004_median_of_two_sorted_arrays.py)
  - 🧠 **MLSys Connection**: In distributed databases or multi-GPU pipeline parallelisms, we often need to merge and find the median of sorted, partitioned chunks. Performing binary search on partition lines in the smaller array resolves this in O(log(min(M, N))) time.

---
### 📅 Day 10 - Tree Recursion & BFS

- **LeetCode 104**: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | **[Easy]**
  - 🔑 **Key Points**: DFS Post-Order Recursion
  - 💻 **Local Template**: [sprint_plan/templates/day10_q104_maximum_depth_of_binary_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day10_q104_maximum_depth_of_binary_tree.py)
  - 🧠 **MLSys Connection**: The recursion depth of a binary tree determines the call stack depth. When writing AST (Abstract Syntax Tree) parsers or computational graph execution engines, we must account for call stack limits (worst-case stack overflow if the tree degenerates into a list of size N).

- **LeetCode 226**: [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | **[Easy]**
  - 🔑 **Key Points**: In-Place Subtree Swapping
  - 💻 **Local Template**: [sprint_plan/templates/day10_q226_invert_binary_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day10_q226_invert_binary_tree.py)
  - 🧠 **MLSys Connection**: A classic structural transformation. It tests fundamental binary tree recursion, return values handling, and in-place child pointer swaps.

- **LeetCode 102**: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | **[Medium]**
  - 🔑 **Key Points**: BFS Level-by-Level Queue
  - 💻 **Local Template**: [sprint_plan/templates/day10_q102_binary_tree_level_order_traversal.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day10_q102_binary_tree_level_order_traversal.py)
  - 🧠 **MLSys Connection**: Level order traversal is the basis of BFS. In graph execution engines and distributed schedulers (e.g. Ray executing dataflow tasks by dependency layer), processing nodes level-by-level ensures strict causal order.

---
### 📅 Day 11 - BST & LCA

- **LeetCode 98**: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | **[Medium]**
  - 🔑 **Key Points**: BST Bounds Propagation
  - 💻 **Local Template**: [sprint_plan/templates/day11_q098_validate_binary_search_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day11_q098_validate_binary_search_tree.py)
  - 🧠 **MLSys Connection**: BST validation is a global property. We must pass valid open interval ranges `(lower, upper)` down to children during recursion. Simply checking if local child nodes satisfy local invariants is a common trap.

- **LeetCode 235**: [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | **[Medium]**
  - 🔑 **Key Points**: BST Path Partitioning
  - 💻 **Local Template**: [sprint_plan/templates/day11_q235_lowest_common_ancestor_of_a_binary_search_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day11_q235_lowest_common_ancestor_of_a_binary_search_tree.py)
  - 🧠 **MLSys Connection**: If both targets are smaller than current, go left; if larger, go right; else the paths split and current is the LCA. Leveraging BST ordering yields an O(H) time and O(1) space optimal solution.

- **LeetCode 236**: [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | **[Medium]**
  - 🔑 **Key Points**: General Binary Tree Post-Order DFS
  - 💻 **Local Template**: [sprint_plan/templates/day11_q236_lowest_common_ancestor_of_a_binary_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day11_q236_lowest_common_ancestor_of_a_binary_tree.py)
  - 🧠 **MLSys Connection**: General trees do not have value ordering, requiring a post-order traversal to bubble up match flags. If left and right subtrees both return non-null, the current node is the LCA.

---
### 📅 Day 12 - Tree Construction & DFS

- **LeetCode 105**: [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | **[Medium]**
  - 🔑 **Key Points**: Pre/In-Order Partition + Hash Mapping
  - 💻 **Local Template**: [sprint_plan/templates/day12_q105_construct_binary_tree_from_preorder_and_inorder_traversal.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day12_q105_construct_binary_tree_from_preorder_and_inorder_traversal.py)
  - 🧠 **MLSys Connection**: In compiler parsers, building an AST from a token sequence and in-order grammar rules is a core compiler task. Caching in-order indices in a hash map optimizes reconstruction time complexity from O(N^2) to O(N).

- **LeetCode 437**: [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | **[Medium]**
  - 🔑 **Key Points**: DFS + Prefix Sum Hash Map
  - 💻 **Local Template**: [sprint_plan/templates/day12_q437_path_sum_iii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day12_q437_path_sum_iii.py)
  - 🧠 **MLSys Connection**: Porting prefix sum logic to trees. During DFS, we maintain running prefix sums in a hash map, backtracking to remove current paths when returning. This yields an O(N) time and O(H) space solution.

- **LeetCode 124**: [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | **[Hard]**
  - 🔑 **Key Points**: DFS + Bent Path Global Update
  - 💻 **Local Template**: [sprint_plan/templates/day12_q124_binary_tree_maximum_path_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day12_q124_binary_tree_maximum_path_sum.py)
  - 🧠 **MLSys Connection**: A classic tree dynamic programming problem. In Critical Path Method (CPM) analyses of computation graphs (determining which sequence of operators is the bottlenecks), this path accumulation logic is used to identify the slowest execution chain.

---
### 📅 Day 13 - Backtracking Basics

- **LeetCode 78**: [Subsets](https://leetcode.com/problems/subsets/) | **[Medium]**
  - 🔑 **Key Points**: Backtracking / Bitmasking
  - 💻 **Local Template**: [sprint_plan/templates/day13_q078_subsets.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day13_q078_subsets.py)
  - 🧠 **MLSys Connection**: Generating subsets is equivalent to traversing a decision tree. In AI compiler operator fusion search space, we evaluate all subset combinations of nodes to find the best kernel fusion plan. Search space size is 2^N.

- **LeetCode 46**: [Permutations](https://leetcode.com/problems/permutations/) | **[Medium]**
  - 🔑 **Key Points**: Decision Tree + Visited Array
  - 💻 **Local Template**: [sprint_plan/templates/day13_q046_permutations.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day13_q046_permutations.py)
  - 🧠 **MLSys Connection**: Permutations represent task scheduling setups. Schedulers run permutations to evaluate all potential task execution orders for instruction-level scheduling optimizations.

- **LeetCode 39**: [Combination Sum](https://leetcode.com/problems/combination-sum/) | **[Medium]**
  - 🔑 **Key Points**: Backtracking + Index Deduplication
  - 💻 **Local Template**: [sprint_plan/templates/day13_q039_combination_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day13_q039_combination_sum.py)
  - 🧠 **MLSys Connection**: Solving combination sums. By passing a `start` search index, we avoid duplicate combinations, demonstrating the basic backtracking constraint patterns.

---
### 📅 Day 14 - Advanced Backtracking

- **LeetCode 51**: [N-Queens](https://leetcode.com/problems/n-queens/) | **[Hard]**
  - 🔑 **Key Points**: Backtracking + Diagonal Hash Tables
  - 💻 **Local Template**: [sprint_plan/templates/day14_q051_n_queens.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day14_q051_n_queens.py)
  - 🧠 **MLSys Connection**: Classic N-Queens backtracking. The key optimization is using arrays for `r - c` and `r + c` to identify diagonals, enabling O(1) conflict validation instead of O(N) board scans.

- **LeetCode 212**: [Word Search II](https://leetcode.com/problems/word-search-ii/) | **[Hard]**
  - 🔑 **Key Points**: Trie + Grid DFS Backtracking + Pruning
  - 💻 **Local Template**: [sprint_plan/templates/day14_q212_word_search_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day14_q212_word_search_ii.py)
  - 🧠 **MLSys Connection**: Build a Trie from target words. Walk the grid and Trie pointers simultaneously. To pass tight limits, when a word is matched, we remove it from the Trie, and prune empty subtrees in-place, eliminating redundant traversal paths.

---
## Phase 3: Graphs & Systems Data Structures (Days 15-21)
**Phase Target**: Master topological sort for task scheduling, Union-Find for connectivity, Trie prefixes, heap scheduling, and hand-code high-performance concurrent Cache systems (LRU/LFU).

### 📅 Day 15 - Graph Traversals

- **LeetCode 200**: [Number of Islands](https://leetcode.com/problems/number-of-islands/) | **[Medium]**
  - 🔑 **Key Points**: Grid BFS / DFS Connectivity
  - 💻 **Local Template**: [sprint_plan/templates/day15_q200_number_of_islands.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day15_q200_number_of_islands.py)
  - 🧠 **MLSys Connection**: In MLSys tensor computational graph partitioning, splitting massive execution graphs into independent subgraphs for distributed training is identical to finding connected island components. In-place modification is used to save memory.

- **LeetCode 133**: [Clone Graph](https://leetcode.com/problems/clone-graph/) | **[Medium]**
  - 🔑 **Key Points**: Hash Map + DFS / BFS Deep Copy
  - 💻 **Local Template**: [sprint_plan/templates/day15_q133_clone_graph.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day15_q133_clone_graph.py)
  - 🧠 **MLSys Connection**: In deep learning compiler IR optimizations or computational graph serialization, we must copy graphs containing cycles (e.g. recurrent neural networks). Maintaining an `old_node -> new_node` hash map prevents infinite recursion loop traps.

- **LeetCode 417**: [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | **[Medium]**
  - 🔑 **Key Points**: Multi-Source Reverse DFS from Boundaries
  - 💻 **Local Template**: [sprint_plan/templates/day15_q417_pacific_atlantic_water_flow.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day15_q417_pacific_atlantic_water_flow.py)
  - 🧠 **MLSys Connection**: Multi-source reverse search. Instead of searching down to ocean boundaries from each cell (which times out), we search uphill from the boundaries. This yields a clean O(M*N) marking of double-reachability.

---
### 📅 Day 16 - Topological Sort & Scheduling

- **LeetCode 207**: [Course Schedule](https://leetcode.com/problems/course-schedule/) | **[Medium]**
  - 🔑 **Key Points**: Kahn's BFS In-Degree Algorithm
  - 💻 **Local Template**: [sprint_plan/templates/day16_q207_course_schedule.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day16_q207_course_schedule.py)
  - 🧠 **MLSys Connection**: Modern ML frameworks (PyTorch, TensorFlow) structure execution DAGs (Directed Acyclic Graphs). Prerequisite dependencies represent edges. The compiler schedules operator executions in topological order to satisfy dependency constraints.

- **LeetCode 210**: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | **[Medium]**
  - 🔑 **Key Points**: Topological Sequence Output
  - 💻 **Local Template**: [sprint_plan/templates/day16_q210_course_schedule_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day16_q210_course_schedule_ii.py)
  - 🧠 **MLSys Connection**: Similar to 207, but collects dequeued nodes. If the sequence length matches the total nodes, the graph is a DAG, return the sorted list, otherwise return empty due to circular deadlock dependencies.

- **LeetCode 269**: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | **[Hard]**
  - 🔑 **Key Points**: DFS Cycle Detection + Reverse Finish Order
  - 💻 **Local Template**: [sprint_plan/templates/day16_q269_alien_dictionary.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day16_q269_alien_dictionary.py)
  - 🧠 **MLSys Connection**: In deep learning compiler instruction schedulers, we infer instruction dependency constraints from adjacent operations. Constructing directed edges and running a topological sort resolves execution priorities.

---
### 📅 Day 17 - Union-Find & Equivalence Classes

- **LeetCode 261**: [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | **[Medium]**
  - 🔑 **Key Points**: Union-Find Cycle and Connectivity Checks
  - 💻 **Local Template**: [sprint_plan/templates/day17_q261_graph_valid_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day17_q261_graph_valid_tree.py)
  - 🧠 **MLSys Connection**: Union-Find is the optimal structure for grouping disjoint equivalence classes. An undirected graph is a tree if edges = n-1 and Union-Find finds no cycles (unioning two nodes already in the same root set `find(u) == find(v)` yields a cycle).

- **LeetCode 323**: [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | **[Medium]**
  - 🔑 **Key Points**: Union-Find Component Counter
  - 💻 **Local Template**: [sprint_plan/templates/day17_q323_number_of_connected_components_in_an_undirected_graph.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day17_q323_number_of_connected_components_in_an_undirected_graph.py)
  - 🧠 **MLSys Connection**: Initialize component count to n. For each successful merge of disjoint sets, decrement count by 1. Union-Find with path compression and rank-based unioning executes in near-constant O(1) amortized time per operation.

- **LeetCode 684**: [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | **[Medium]**
  - 🔑 **Key Points**: Union-Find Cycle Pinpointing
  - 💻 **Local Template**: [sprint_plan/templates/day17_q684_redundant_connection.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day17_q684_redundant_connection.py)
  - 🧠 **MLSys Connection**: In redundant network routing path pruning, we locate the final edge that creates a loop. Processing edges sequentially with Union-Find identifies the first cycle-creating edge in O(E) time.

---
### 📅 Day 18 - Prefix Trees (Trie)

- **LeetCode 208**: [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | **[Medium]**
  - 🔑 **Key Points**: Nested Hash Map Children Nodes
  - 💻 **Local Template**: [sprint_plan/templates/day18_q208_implement_trie_prefix_tree.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day18_q208_implement_trie_prefix_tree.py)
  - 🧠 **MLSys Connection**: In Large Language Model (LLM) speculative decoding, serving engines use Tries to index vocabularies, enabling fast prefix constraints validation and KV Cache token matches, drastically reducing sequence comparisons.

- **LeetCode 211**: [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | **[Medium]**
  - 🔑 **Key Points**: Trie Wildcard Search via DFS
  - 💻 **Local Template**: [sprint_plan/templates/day18_q211_design_add_and_search_words_data_structure.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day18_q211_design_add_and_search_words_data_structure.py)
  - 🧠 **MLSys Connection**: Extends standard Trie search with wildcard '.' handling. When encountering '.', we recursively check all child branches of the current node, demonstrating recursive Trie search patterns.

- **LeetCode 642**: [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/) | **[Hard]**
  - 🔑 **Key Points**: Trie + Min-Heap Top-K Filter
  - 💻 **Local Template**: [sprint_plan/templates/day18_q642_design_search_autocomplete_system.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day18_q642_design_search_autocomplete_system.py)
  - 🧠 **MLSys Connection**: Simulating search engine auto-complete. In speculative decoding or prefix tuning, filtering high-frequency predictions based on string prefixes represents a critical performance path.

---
### 📅 Day 19 - Heaps & Priority Schedulers

- **LeetCode 23**: [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | **[Hard]**
  - 🔑 **Key Points**: Min-Heap Node Tracking / Divide & Conquer
  - 💻 **Local Template**: [sprint_plan/templates/day19_q023_merge_k_sorted_lists.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day19_q023_merge_k_sorted_lists.py)
  - 🧠 **MLSys Connection**: In distributed stream mergers or log consolidation engines, a min-heap tracks the current head of k sorted streams. This runs in O(N log k) time and represents a core scheduling technique in database log mergers.

- **LeetCode 347**: [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | **[Medium]**
  - 🔑 **Key Points**: Hash Map + Bucket Sort (O(N) Optimal)
  - 💻 **Local Template**: [sprint_plan/templates/day19_q347_top_k_frequent_elements.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day19_q347_top_k_frequent_elements.py)
  - 🧠 **MLSys Connection**: While a min-heap gives O(N log K), the optimal solution uses bucket sort. Because frequencies are bounded by `[0, N]`, bucket sorting allows linear O(N) retrieval, highlighting a data-driven system optimization choice.

- **LeetCode 295**: [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | **[Hard]**
  - 🔑 **Key Points**: Dual Balanced Heaps (Max & Min)
  - 💻 **Local Template**: [sprint_plan/templates/day19_q295_find_median_from_data_stream.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day19_q295_find_median_from_data_stream.py)
  - 🧠 **MLSys Connection**: In MLSys runtime telemetry modules, we must compute the median inference latency in O(1) time while accepting new data points in O(log N) time. This is solved by balancing a Max-Heap (smaller values) and a Min-Heap (larger values).

---
### 📅 Day 20 - Bit Manipulation & Lower-Precision Formats

- **LeetCode 136**: [Single Number](https://leetcode.com/problems/single-number/) | **[Easy]**
  - 🔑 **Key Points**: Bitwise XOR properties (a ^ a = 0)
  - 💻 **Local Template**: [sprint_plan/templates/day20_q136_single_number.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q136_single_number.py)
  - 🧠 **MLSys Connection**: XOR properties (`x ^ x = 0`, `x ^ 0 = x`) and associativity allow O(N) scan in O(1) space. This is a common parity check and data validation technique in hardware-constrained embedded applications.

- **LeetCode 338**: [Counting Bits](https://leetcode.com/problems/counting-bits/) | **[Easy]**
  - 🔑 **Key Points**: DP Bitwise Recurrence
  - 💻 **Local Template**: [sprint_plan/templates/day20_q338_counting_bits.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q338_counting_bits.py)
  - 🧠 **MLSys Connection**: Using `dp[i] = dp[i >> 1] + (i & 1)` computes set bits for all numbers from 0 to N in O(N) time. Used in quantized weights bitwidth profiling for Binary Neural Networks (BNNs) and INT8 model quantization.

- **LeetCode 190**: [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | **[Easy]**
  - 🔑 **Key Points**: Bitwise Shifts & Accumulation
  - 💻 **Local Template**: [sprint_plan/templates/day20_q190_reverse_bits.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q190_reverse_bits.py)
  - 🧠 **MLSys Connection**: Bitwise swaps. Required for network packet conversions (Big-endian to Little-endian byte order transformations) and graphics pixel bit alignment.

- **LeetCode 137**: [Single Number II](https://leetcode.com/problems/single-number-ii/) | **[Medium]**
  - 🔑 **Key Points**: Bit-position Modulo Arithmetic
  - 💻 **Local Template**: [sprint_plan/templates/day20_q137_single_number_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day20_q137_single_number_ii.py)
  - 🧠 **MLSys Connection**: Simulating logic gates in hardware accelerators (ASICs/FPGAs) or SIMD vector optimizations to track duplicate cycles without using general registers.

---
### 📅 Day 21 - Cache System Implementation

- **LeetCode 146**: [LRU Cache](https://leetcode.com/problems/lru-cache/) | **[Medium]**
  - 🔑 **Key Points**: Hash Map + Doubly Linked List (O(1))
  - 💻 **Local Template**: [sprint_plan/templates/day21_q146_lru_cache.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day21_q146_lru_cache.py)
  - 🧠 **MLSys Connection**: A primary MLSys design challenge. LRU page eviction is the default mechanism for LLM KV Cache paging (e.g. vLLM's PagedAttention) and deep learning Parameter Server weight swapping. You must hand-code it in O(1) time using a hash map and a doubly linked list. Often extended to discuss thread safety via shared reader-writer locks (shared_mutex) or fine-grained bucket locks in concurrent implementations.

- **LeetCode 460**: [LFU Cache](https://leetcode.com/problems/lfu-cache/) | **[Hard]**
  - 🔑 **Key Points**: Double Hash Maps + Frequency Lists
  - 💻 **Local Template**: [sprint_plan/templates/day21_q460_lfu_cache.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day21_q460_lfu_cache.py)
  - 🧠 **MLSys Connection**: Hard cache eviction. Evicts the least frequently used node, breaking ties using LRU. Requires maintaining a `min_freq` integer and a mapping of frequencies to doubly linked lists, challenging data structure composition skills.

- **LeetCode 622**: [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | **[Medium]**
  - 🔑 **Key Points**: Circular Array Modulo Arithmetic
  - 💻 **Local Template**: [sprint_plan/templates/day21_q622_design_circular_queue.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day21_q622_design_circular_queue.py)
  - 🧠 **MLSys Connection**: Ring buffers are the standard data structures for OS IPC (Inter-Process Communication), producer-consumer loops, and GPU command queues. Modulo index updates `(tail + 1) % size` enable lock-free concurrent ring buffer queues.

---
## Phase 4: Dynamic Programming & High-Pressure Mock (Days 22-30)
**Phase Target**: Master 1D/2D state transitions, apply space compression optimizations, and practice solving unseen tasks under strict time-box constraints.

### 📅 Day 22 - 1D Dynamic Programming

- **LeetCode 70**: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | **[Easy]**
  - 🔑 **Key Points**: 1D Recurrence + Space Compression
  - 💻 **Local Template**: [sprint_plan/templates/day22_q070_climbing_stairs.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day22_q070_climbing_stairs.py)
  - 🧠 **MLSys Connection**: Basic dynamic programming. Rolling variables `a, b = b, a + b` compress space from O(N) to O(1). In MLSys tensor compilers, minimizing memory footprint via buffer reuse is a key optimization goal.

- **LeetCode 746**: [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | **[Easy]**
  - 🔑 **Key Points**: Weighted 1D DP Recurrence
  - 💻 **Local Template**: [sprint_plan/templates/day22_q746_min_cost_climbing_stairs.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day22_q746_min_cost_climbing_stairs.py)
  - 🧠 **MLSys Connection**: DP recurrence `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`. Can be optimized to O(1) space, helping to build basic dynamic programming muscle memory.

- **LeetCode 322**: [Coin Change](https://leetcode.com/problems/coin-change/) | **[Medium]**
  - 🔑 **Key Points**: Unbounded Knapsack - Bottom-Up DP
  - 💻 **Local Template**: [sprint_plan/templates/day22_q322_coin_change.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day22_q322_coin_change.py)
  - 🧠 **MLSys Connection**: Optimization problem where greedy choices fail. Transition equation: `dp[i] = min(dp[i], dp[i - coin] + 1)`. In runtime system resource scheduler budget allocations, knapsack allocation models are widely applied.

---
### 📅 Day 23 - Subsequences & Knapsack DP

- **LeetCode 300**: [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | **[Medium]**
  - 🔑 **Key Points**: Patience Sorting / Greedy + Binary Search
  - 💻 **Local Template**: [sprint_plan/templates/day23_q300_longest_increasing_subsequence.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day23_q300_longest_increasing_subsequence.py)
  - 🧠 **MLSys Connection**: Optimal O(N log N) using greedy tail replacements and binary search. In compiler instruction pipelining, identifying longest non-dependent instruction sequences dictates parallel execution schedules.

- **LeetCode 139**: [Word Break](https://leetcode.com/problems/word-break/) | **[Medium]**
  - 🔑 **Key Points**: Prefix Partitioning DP + Hash Set
  - 💻 **Local Template**: [sprint_plan/templates/day23_q139_word_break.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day23_q139_word_break.py)
  - 🧠 **MLSys Connection**: Evaluating segmentations of contiguous streams. Transition: `dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`. In compiler lexical parsing and token segmentations, prefix partitioning plays a central role.

- **LeetCode 416**: [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | **[Medium]**
  - 🔑 **Key Points**: 0-1 Knapsack with Space Compression
  - 💻 **Local Template**: [sprint_plan/templates/day23_q416_partition_equal_subset_sum.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day23_q416_partition_equal_subset_sum.py)
  - 🧠 **MLSys Connection**: Classic 0-1 knapsack. To compress space, we update a 1D DP array backwards (from right to left) to prevent using values updated in the current iteration, dropping space from O(target) to O(target).

---
### 📅 Day 24 - 2D Grid Dynamic Programming

- **LeetCode 62**: [Unique Paths](https://leetcode.com/problems/unique-paths/) | **[Medium]**
  - 🔑 **Key Points**: Grid DP + Row Rolling Compression
  - 💻 **Local Template**: [sprint_plan/templates/day24_q062_unique_paths.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day24_q062_unique_paths.py)
  - 🧠 **MLSys Connection**: Grid routing. Transition: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. In Network-on-Chip (NoC) hardware routing designs, analyzing packet routing paths matches this model. Space can be compressed to a 1D row array.

- **LeetCode 1143**: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | **[Medium]**
  - 🔑 **Key Points**: 2D Alignment DP Matrix
  - 💻 **Local Template**: [sprint_plan/templates/day24_q1143_longest_common_subsequence.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day24_q1143_longest_common_subsequence.py)
  - 🧠 **MLSys Connection**: LCS is the core algorithm for compiler code-diff checkers and structural network similarity evaluations. Time complexity is O(M*N), and rolling row array updates are often asked in system memory optimization rounds.

- **LeetCode 72**: [Edit Distance](https://leetcode.com/problems/edit-distance/) | **[Hard]**
  - 🔑 **Key Points**: 2D Match Decision Matrix
  - 💻 **Local Template**: [sprint_plan/templates/day24_q072_edit_distance.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day24_q072_edit_distance.py)
  - 🧠 **MLSys Connection**: Minimum edit cost calculation. Analyzing state transitions from three cells `dp[i-1][j]`, `dp[i][j-1]`, and `dp[i-1][j-1]` evaluates comprehensive 2D dynamic programming logic.

---
### 📅 Day 25 - Interval & Tree DP

- **LeetCode 96**: [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | **[Medium]**
  - 🔑 **Key Points**: Catalan Number Recurrence
  - 💻 **Local Template**: [sprint_plan/templates/day25_q096_unique_binary_search_trees.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day25_q096_unique_binary_search_trees.py)
  - 🧠 **MLSys Connection**: Counting possible BST shapes. Summing the product of left and right child permutations derives the Catalan recurrence, showcasing algebraic state symmetry.

- **LeetCode 337**: [House Robber III](https://leetcode.com/problems/house-robber-iii/) | **[Medium]**
  - 🔑 **Key Points**: Tree DP + State Tuple DFS Propagation
  - 💻 **Local Template**: [sprint_plan/templates/day25_q337_house_robber_iii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day25_q337_house_robber_iii.py)
  - 🧠 **MLSys Connection**: In computational graph kernel fusions, selecting optimal operator combinations where adjacent nodes cannot be fused matches tree DP. DFS returns a tuple `(fuse, skip)`, constraining time complexity to O(N).

- **LeetCode 312**: [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | **[Hard]**
  - 🔑 **Key Points**: Interval DP (Bottom-Up)
  - 💻 **Local Template**: [sprint_plan/templates/day25_q312_burst_balloons.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day25_q312_burst_balloons.py)
  - 🧠 **MLSys Connection**: Advanced interval DP. Reversing the problem to identify 'which balloon is popped last' separates the interval into independent segments, defining the state transition. Crucial for complex compiler scheduler optimizations.

---
### 📅 Day 26 - Greedy Algorithms

- **LeetCode 55**: [Jump Game](https://leetcode.com/problems/jump-game/) | **[Medium]**
  - 🔑 **Key Points**: Greedy - Backwards Goal Shifting
  - 💻 **Local Template**: [sprint_plan/templates/day26_q055_jump_game.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day26_q055_jump_game.py)
  - 🧠 **MLSys Connection**: Evaluating if a resource packet can route across nodes with variable reach capabilities. Shifting `goal` backwards from the end runs in O(N) time and O(1) space, which is far superior to standard 1D DP (O(N^2)).

- **LeetCode 134**: [Gas Station](https://leetcode.com/problems/gas-station/) | **[Medium]**
  - 🔑 **Key Points**: Net Sum Check + Greedy Pivot Search
  - 💻 **Local Template**: [sprint_plan/templates/day26_q134_gas_station.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day26_q134_gas_station.py)
  - 🧠 **MLSys Connection**: If total supply exceeds total consumption, a solution must exist. A single scan shifts the starting candidate to `i + 1` whenever the rolling sum drops below 0, optimizing the O(N^2) search to O(N).

- **LeetCode 406**: [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | **[Medium]**
  - 🔑 **Key Points**: Greedy Insertion after Multi-Key Sort
  - 💻 **Local Template**: [sprint_plan/templates/day26_q406_queue_reconstruction_by_height.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day26_q406_queue_reconstruction_by_height.py)
  - 🧠 **MLSys Connection**: Scheduling multi-resource allocations with two priorities. Sorting height descending and queue index ascending, then executing index insertions, yields the local queue reconstruction.

---
### 📅 Day 27 - Intervals & Scheduling

- **LeetCode 56**: [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | **[Medium]**
  - 🔑 **Key Points**: Sort by Start Time + Linear Merge
  - 💻 **Local Template**: [sprint_plan/templates/day27_q056_merge_intervals.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day27_q056_merge_intervals.py)
  - 🧠 **MLSys Connection**: In OS virtual memory managers, when pages are deallocated, contiguous free blocks are coalesced (merged) to minimize memory fragmentation. Coalescing free blocks is logically equivalent to interval merging.

- **LeetCode 435**: [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | **[Medium]**
  - 🔑 **Key Points**: Greedy - Sort by End Time
  - 💻 **Local Template**: [sprint_plan/templates/day27_q435_non_overlapping_intervals.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day27_q435_non_overlapping_intervals.py)
  - 🧠 **MLSys Connection**: Classic interval scheduling. To maximize scheduled tasks, prioritize intervals that end earliest. Used in real-time priority task scheduling and instruction pipelines.

- **LeetCode 621**: [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | **[Medium]**
  - 🔑 **Key Points**: Greedy Bucket Fill with Cooldowns
  - 💻 **Local Template**: [sprint_plan/templates/day27_q621_task_scheduler.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day27_q621_task_scheduler.py)
  - 🧠 **MLSys Connection**: In CPU schedulers or GPU thread dispatchers, tasks of the same type must wait for a Cooldown cycle. Estimating cycles by filling buckets with high-frequency tasks resolves the scheduling pattern in O(N) time.

---
### 📅 Day 28 - Mock Simulator Day 1 (Google/Meta Core Systems)

- **LeetCode 307**: [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | **[Hard]**
  - 🔑 **Key Points**: Segment Tree / Binary Indexed Tree
  - 💻 **Local Template**: [sprint_plan/templates/day28_q307_range_sum_query___mutable.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day28_q307_range_sum_query___mutable.py)
  - 🧠 **MLSys Connection**: In dynamic ML tensors where values are frequently mutated and range sums are queried, prefix sums cost O(N) updates. Segment Trees or Fenwick Trees optimize both operations to O(log N) time, demonstrating query-update balance.

- **LeetCode 588**: [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) | **[Hard]**
  - 🔑 **Key Points**: Trie with File Node Directory Tree
  - 💻 **Local Template**: [sprint_plan/templates/day28_q588_design_in_memory_file_system.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day28_q588_design_in_memory_file_system.py)
  - 🧠 **MLSys Connection**: Designing an OS in-memory file system. Models a directory hierarchy using a Trie where terminal nodes represent file contents, supporting `ls`, `mkdir`, `addContentToFile`, and `readContentFromFile` operations.

---
### 📅 Day 29 - Mock Simulator Day 2 (NVIDIA/Apple Hardware & Concurrency)

- **LeetCode 311**: [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) | **[Medium]**
  - 🔑 **Key Points**: Compressed Row Storage (CRS / CSR) Optimization
  - 💻 **Local Template**: [sprint_plan/templates/day29_q311_sparse_matrix_multiplication.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day29_q311_sparse_matrix_multiplication.py)
  - 🧠 **MLSys Connection**: The core kernel of Sparse Neural Networks. In GPU computations, performing dense multiplications on massive zero arrays wastes memory bandwidth. Iterating only over non-zero elements using Row-major formats simulates CSR acceleration hardware kernels.

- **LeetCode 380**: [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | **[Medium]**
  - 🔑 **Key Points**: Hash Map + Dynamic Array Tail Swap
  - 💻 **Local Template**: [sprint_plan/templates/day29_q380_insert_delete_getrandom_o1.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day29_q380_insert_delete_getrandom_o1.py)
  - 🧠 **MLSys Connection**: Used in MLSys negative batch samplers requiring O(1) random draws, inserts, and deletes. A map indexes keys to list offsets. To delete in O(1) time, swap the target element with the last element of the list, then pop back to avoid array shifting.

---
### 📅 Day 30 - Mock Simulator Day 3 (FAANG Hard Graduation Challenges)

- **LeetCode 460**: [LFU Cache](https://leetcode.com/problems/lfu-cache/) | **[Hard]**
  - 🔑 **Key Points**: Hand-Code LFU (Review Day 21)
  - 💻 **Local Template**: [sprint_plan/templates/day30_q460_lfu_cache.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day30_q460_lfu_cache.py)
  - 🧠 **MLSys Connection**: High-performance cache design under pressure. Evict least-frequently-used nodes, requiring double hash maps and frequency doubly linked list updates in O(1) time.

- **LeetCode 212**: [Word Search II](https://leetcode.com/problems/word-search-ii/) | **[Hard]**
  - 🔑 **Key Points**: Hand-Code Trie + Backtracking Grid DFS (Review Day 14)
  - 💻 **Local Template**: [sprint_plan/templates/day30_q212_word_search_ii.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day30_q212_word_search_ii.py)
  - 🧠 **MLSys Connection**: Integrates Tries, matrix traversals, backtracking, and recursive parent pruning optimizations. Evaluates graph searches and pruning under tight limits.

- **LeetCode 269**: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | **[Hard]**
  - 🔑 **Key Points**: Hand-Code Topological Sort & DFS Cycle Detect (Review Day 16)
  - 💻 **Local Template**: [sprint_plan/templates/day30_q269_alien_dictionary.py](file:///D:/OneDrive - purdue.edu/Academic/GitHub/blind75/blind75_study_pack/sprint_plan/templates/day30_q269_alien_dictionary.py)
  - 🧠 **MLSys Connection**: The foundation of compilation pipeline dependencies scheduling. Combines parsing, directed graph construction, cycle validation, and topological sorting.

---