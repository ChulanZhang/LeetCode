# -*- coding: utf-8 -*-

PHASES = [
    {
        "name": "Phase 1: Foundations & Pointer Intuition (Days 1-7)",
        "target": "Master two pointers (left-right, fast-slow), sliding windows, monotonic stacks/queues, and prefix sums. Build strong memory muscle for array/list transformations and eliminate boundary pointer bugs.",
        "days": {
            1: {
                "theme": "Arrays & Two Pointers",
                "problems": [
                    {"id": "1", "name": "Two Sum", "difficulty": "Easy", "key": "Hash Map / Two Pointers", "systems_note": "Utilizing static hash maps or sorted two-pointer matching is the standard approach for fast table lookups in low-level systems and GPU kernel designs. Optimizing from O(N^2) to O(N) is a classic space-time tradeoff example."},
                    {"id": "15", "name": "3Sum", "difficulty": "Medium", "key": "Sorting + Left-Right Pointers", "systems_note": "The core of two-pointer searches is search space reduction using monotonicity. Sorting allows us to shift pointers inwards conditionally, pruning the brute-force O(N^3) search space to O(N^2)."},
                    {"id": "11", "name": "Container With Most Water", "difficulty": "Medium", "key": "Two Pointers + Greedy Shifting", "systems_note": "Greedy algorithms are crucial in system scheduling (e.g. choosing nodes with the lowest network latency). Moving the pointer pointing to the shorter line is the only action that can potentially yield a larger area."}
                ]
            },
            2: {
                "theme": "Sliding Window",
                "problems": [
                    {"id": "3", "name": "Longest Substring Without Repeating Characters", "difficulty": "Medium", "key": "Sliding Window + Hash Set", "systems_note": "Sliding window is the standard pattern for contiguous sub-array problems. It is widely used in network protocol layers (e.g. TCP sliding window congestion control) and stream processing systems (e.g. computing average request rates over a sliding temporal window)."},
                    {"id": "424", "name": "Longest Repeating Character Replacement", "difficulty": "Medium", "key": "Sliding Window + Freq Tracking", "systems_note": "The window condition is that window length L minus the frequency of the most frequent character `max_freq` must be <= k. We maintain a historical `max_freq` to avoid scanning the frequency map of size 26 on every window contraction."},
                    {"id": "76", "name": "Minimum Window Substring", "difficulty": "Hard", "key": "Sliding Window + Dual Hash Maps", "systems_note": "A benchmark problem for hard sliding windows. In compiler lexical analyzers and low-level pattern scanners, similar sliding window logic is used for high-performance syntax token parsing."}
                ]
            },
            3: {
                "theme": "Fast & Slow Pointers",
                "problems": [
                    {"id": "141", "name": "Linked List Cycle", "difficulty": "Easy", "key": "Floyd's Cycle-Finding Algorithm", "systems_note": "Fast and slow pointers are used in OS memory managers to detect if free memory blocks or page descriptors have circular pointer references (which causes memory leak traps or segmentation faults) due to corrupt allocations."},
                    {"id": "142", "name": "Linked List Cycle II", "difficulty": "Medium", "key": "Floyd's Algorithm for Loop Entry", "systems_note": "Mathematical proof shows that the distance from the head to the loop entry equals the distance from the pointer meeting point to the loop entry. This demonstrates precise pointer distance manipulation."},
                    {"id": "202", "name": "Happy Number", "difficulty": "Easy", "key": "Implicit Linked List Cycle Detection", "systems_note": "Transformations of a number can be modeled as a directed graph where nodes have out-degree 1 (analogous to a singly linked list). Circular dependency detection can be solved using fast and slow pointers in O(1) auxiliary space."}
                ]
            },
            4: {
                "theme": "Monotonic Stack",
                "problems": [
                    {"id": "496", "name": "Next Greater Element I", "difficulty": "Easy", "key": "Monotonic Decreasing Stack", "systems_note": "Monotonic stacks are optimal for 'finding the next greater element'. By maintaining stack monotonicity, we guarantee each element is pushed and popped at most once, achieving a linear O(N) time complexity."},
                    {"id": "739", "name": "Daily Temperatures", "difficulty": "Medium", "key": "Monotonic Stack Storing Indices", "systems_note": "In time-series analysis and system latency metric telemetry (e.g. finding the next timestamp where queue latency drops below a threshold), monotonic stack-based index tracking is a fundamental building block."},
                    {"id": "84", "name": "Largest Rectangle in Histogram", "difficulty": "Hard", "key": "Monotonic Increasing Stack + Sentinels", "systems_note": "Used in memory defragmentation (e.g. finding the largest contiguous blocks of physical memory pages). The algorithm calculates areas from the popped taller blocks in O(N) time."}
                ]
            },
            5: {
                "theme": "Monotonic Queue",
                "problems": [
                    {"id": "239", "name": "Sliding Window Maximum", "difficulty": "Hard", "key": "Monotonic Queue (Double-Ended Queue)", "systems_note": "In MLSys inference servers, we must compute sliding window metrics such as peak inference latency or throughput. Using a double-ended queue (deque) to maintain monotonicity ensures O(N) time complexity for real-time monitoring statistics."},
                    {"id": "862", "name": "Shortest Subarray with Sum at Least K", "difficulty": "Hard", "key": "Prefix Sum + Monotonic Deque", "systems_note": "Finding the shortest subarray satisfying an accumulation threshold in data streams containing negative values. Combining prefix sums with a monotonic deque achieves O(N) optimal search time."}
                ]
            },
            6: {
                "theme": "Prefix Sums & Difference Arrays",
                "problems": [
                    {"id": "304", "name": "Range Sum Query 2D - Immutable", "difficulty": "Medium", "key": "2D Prefix Sums / Integral Image", "systems_note": "A 2D prefix sum is mathematically identical to an 'Integral Image' in computer vision. In CNN (Convolutional Neural Networks) pooling layers or local sum kernels, it optimizes range sum calculations from O(H*W) to O(1)."},
                    {"id": "1109", "name": "Corporate Flight Bookings", "difficulty": "Medium", "key": "1D Difference Array", "systems_note": "Difference arrays are used to handle batch range addition/subtraction. In task scheduling, if we need to allocate resources over a time window, difference arrays allow O(1) updates per request and reconstruction in O(N) time via prefix sums."},
                    {"id": "1094", "name": "Car Pooling", "difficulty": "Medium", "key": "Difference Array Overload Checks", "systems_note": "Used in distributed system concurrency throttling and dynamic GPU memory budget tracking. We convert intervals of resource demands into difference arrays to verify if peak load violates hard hardware capacity constraints."}
                ]
            },
            7: {
                "theme": "Matrix Operations & Locality",
                "problems": [
                    {"id": "48", "name": "Rotate Image", "difficulty": "Medium", "key": "In-Place Transpose + Reflection", "systems_note": "Matrix transpose and reflection inspect Cache Locality. In MLSys, tensor dimensions permutes (Transpose/Permute) are extremely common. Fast strided addressing and in-place swapping on contiguous 1D memory buffers are central to GPU kernel optimization."},
                    {"id": "54", "name": "Spiral Matrix", "difficulty": "Medium", "key": "Boundary Pointer Shrinking Simulation", "systems_note": "Clockwise spiral traversal. It requires strict boundary checks (top, bottom, left, right) to prevent out-of-bounds access, testing precision in array slicing and boundary control."},
                    {"id": "73", "name": "Set Matrix Zeroes", "difficulty": "Medium", "key": "Row/Column Projection Markers", "systems_note": "An in-place marking scheme when memory is extremely constrained. By projecting zero states onto the first row and first column of the matrix, we achieve O(1) auxiliary space, which is highly practical in embedded or edge computing kernels."}
                ]
            }
        }
    },
    {
        "name": "Phase 2: Trees & Binary Search (Days 8-14)",
        "target": "Avoid infinite loops in binary search boundary updates, master recursive derivations of tree/BST structures, and build confidence in backtracking and state space pruning.",
        "days": {
            8: {
                "theme": "Binary Search",
                "problems": [
                    {"id": "704", "name": "Binary Search", "difficulty": "Easy", "key": "Standard Binary Search Template", "systems_note": "The essence of binary search is partition boundary definition and loop condition control. In low-level systems, such as OS memory page table lookup or indexing in sorted key-value databases, binary search is the default O(log N) lookup algorithm."},
                    {"id": "33", "name": "Search in Rotated Sorted Array", "difficulty": "Medium", "key": "Monotonic Half Partitioning", "systems_note": "Search in rotated arrays. If split in half, at least one half of the rotated sorted array is guaranteed to be strictly sorted. Detecting which half is sorted allows us to halve the search space at each step."},
                    {"id": "153", "name": "Find Minimum in Rotated Sorted Array", "difficulty": "Medium", "key": "Inflection Point Binary Search", "systems_note": "Compare `mid` with the right boundary `right`. If `nums[mid] > nums[right]`, the inflection point is in the right half, otherwise in the left. This tests the ability to leverage monotonicity in non-trivially sorted sequences."}
                ]
            },
            9: {
                "theme": "Advanced Binary Search",
                "problems": [
                    {"id": "74", "name": "Search a 2D Matrix", "difficulty": "Medium", "key": "Matrix 1D Flat Indexing", "systems_note": "A row-major sorted matrix is stored contiguously in memory as a 1D array. By mapping indices via `(row, col) = (mid // n, mid % n)`, we run standard binary search directly on the flat memory block, avoiding conversion overhead."},
                    {"id": "162", "name": "Find Peak Element", "difficulty": "Medium", "key": "Hill Climbing Binary Search", "systems_note": "In optimization theory and adaptive parameter tuning, 'Hill Climbing' is the fundamental local search heuristic. If the slope at `mid` is ascending, the peak must lie to the right, which guarantees locating a peak in O(log N) time."},
                    {"id": "4", "name": "Median of Two Sorted Arrays", "difficulty": "Hard", "key": "Binary Search on Array Partitioning", "systems_note": "In distributed databases or multi-GPU pipeline parallelisms, we often need to merge and find the median of sorted, partitioned chunks. Performing binary search on partition lines in the smaller array resolves this in O(log(min(M, N))) time."}
                ]
            },
            10: {
                "theme": "Tree Recursion & BFS",
                "problems": [
                    {"id": "104", "name": "Maximum Depth of Binary Tree", "difficulty": "Easy", "key": "DFS Post-Order Recursion", "systems_note": "The recursion depth of a binary tree determines the call stack depth. When writing AST (Abstract Syntax Tree) parsers or computational graph execution engines, we must account for call stack limits (worst-case stack overflow if the tree degenerates into a list of size N)."},
                    {"id": "226", "name": "Invert Binary Tree", "difficulty": "Easy", "key": "In-Place Subtree Swapping", "systems_note": "A classic structural transformation. It tests fundamental binary tree recursion, return values handling, and in-place child pointer swaps."},
                    {"id": "102", "name": "Binary Tree Level Order Traversal", "difficulty": "Medium", "key": "BFS Level-by-Level Queue", "systems_note": "Level order traversal is the basis of BFS. In graph execution engines and distributed schedulers (e.g. Ray executing dataflow tasks by dependency layer), processing nodes level-by-level ensures strict causal order."}
                ]
            },
            11: {
                "theme": "BST & LCA",
                "problems": [
                    {"id": "98", "name": "Validate Binary Search Tree", "difficulty": "Medium", "key": "BST Bounds Propagation", "systems_note": "BST validation is a global property. We must pass valid open interval ranges `(lower, upper)` down to children during recursion. Simply checking if local child nodes satisfy local invariants is a common trap."},
                    {"id": "235", "name": "Lowest Common Ancestor of a Binary Search Tree", "difficulty": "Medium", "key": "BST Path Partitioning", "systems_note": "If both targets are smaller than current, go left; if larger, go right; else the paths split and current is the LCA. Leveraging BST ordering yields an O(H) time and O(1) space optimal solution."},
                    {"id": "236", "name": "Lowest Common Ancestor of a Binary Tree", "difficulty": "Medium", "key": "General Binary Tree Post-Order DFS", "systems_note": "General trees do not have value ordering, requiring a post-order traversal to bubble up match flags. If left and right subtrees both return non-null, the current node is the LCA."}
                ]
            },
            12: {
                "theme": "Tree Construction & DFS",
                "problems": [
                    {"id": "105", "name": "Construct Binary Tree from Preorder and Inorder Traversal", "difficulty": "Medium", "key": "Pre/In-Order Partition + Hash Mapping", "systems_note": "In compiler parsers, building an AST from a token sequence and in-order grammar rules is a core compiler task. Caching in-order indices in a hash map optimizes reconstruction time complexity from O(N^2) to O(N)."},
                    {"id": "437", "name": "Path Sum III", "difficulty": "Medium", "key": "DFS + Prefix Sum Hash Map", "systems_note": "Porting prefix sum logic to trees. During DFS, we maintain running prefix sums in a hash map, backtracking to remove current paths when returning. This yields an O(N) time and O(H) space solution."},
                    {"id": "124", "name": "Binary Tree Maximum Path Sum", "difficulty": "Hard", "key": "DFS + Bent Path Global Update", "systems_note": "A classic tree dynamic programming problem. In Critical Path Method (CPM) analyses of computation graphs (determining which sequence of operators is the bottlenecks), this path accumulation logic is used to identify the slowest execution chain."}
                ]
            },
            13: {
                "theme": "Backtracking Basics",
                "problems": [
                    {"id": "78", "name": "Subsets", "difficulty": "Medium", "key": "Backtracking / Bitmasking", "systems_note": "Generating subsets is equivalent to traversing a decision tree. In AI compiler operator fusion search space, we evaluate all subset combinations of nodes to find the best kernel fusion plan. Search space size is 2^N."},
                    {"id": "46", "name": "Permutations", "difficulty": "Medium", "key": "Decision Tree + Visited Array", "systems_note": "Permutations represent task scheduling setups. Schedulers run permutations to evaluate all potential task execution orders for instruction-level scheduling optimizations."},
                    {"id": "39", "name": "Combination Sum", "difficulty": "Medium", "key": "Backtracking + Index Deduplication", "systems_note": "Solving combination sums. By passing a `start` search index, we avoid duplicate combinations, demonstrating the basic backtracking constraint patterns."}
                ]
            },
            14: {
                "theme": "Advanced Backtracking",
                "problems": [
                    {"id": "51", "name": "N-Queens", "difficulty": "Hard", "key": "Backtracking + Diagonal Hash Tables", "systems_note": "Classic N-Queens backtracking. The key optimization is using arrays for `r - c` and `r + c` to identify diagonals, enabling O(1) conflict validation instead of O(N) board scans."},
                    {"id": "212", "name": "Word Search II", "difficulty": "Hard", "key": "Trie + Grid DFS Backtracking + Pruning", "systems_note": "Build a Trie from target words. Walk the grid and Trie pointers simultaneously. To pass tight limits, when a word is matched, we remove it from the Trie, and prune empty subtrees in-place, eliminating redundant traversal paths."}
                ]
            }
        }
    },
    {
        "name": "Phase 3: Graphs & Systems Data Structures (Days 15-21)",
        "target": "Master topological sort for task scheduling, Union-Find for connectivity, Trie prefixes, heap scheduling, and hand-code high-performance concurrent Cache systems (LRU/LFU).",
        "days": {
            15: {
                "theme": "Graph Traversals",
                "problems": [
                    {"id": "200", "name": "Number of Islands", "difficulty": "Medium", "key": "Grid BFS / DFS Connectivity", "systems_note": "In MLSys tensor computational graph partitioning, splitting massive execution graphs into independent subgraphs for distributed training is identical to finding connected island components. In-place modification is used to save memory."},
                    {"id": "133", "name": "Clone Graph", "difficulty": "Medium", "key": "Hash Map + DFS / BFS Deep Copy", "systems_note": "In deep learning compiler IR optimizations or computational graph serialization, we must copy graphs containing cycles (e.g. recurrent neural networks). Maintaining an `old_node -> new_node` hash map prevents infinite recursion loop traps."},
                    {"id": "417", "name": "Pacific Atlantic Water Flow", "difficulty": "Medium", "key": "Multi-Source Reverse DFS from Boundaries", "systems_note": "Multi-source reverse search. Instead of searching down to ocean boundaries from each cell (which times out), we search uphill from the boundaries. This yields a clean O(M*N) marking of double-reachability."}
                ]
            },
            16: {
                "theme": "Topological Sort & Scheduling",
                "problems": [
                    {"id": "207", "name": "Course Schedule", "difficulty": "Medium", "key": "Kahn's BFS In-Degree Algorithm", "systems_note": "Modern ML frameworks (PyTorch, TensorFlow) structure execution DAGs (Directed Acyclic Graphs). Prerequisite dependencies represent edges. The compiler schedules operator executions in topological order to satisfy dependency constraints."},
                    {"id": "210", "name": "Course Schedule II", "difficulty": "Medium", "key": "Topological Sequence Output", "systems_note": "Similar to 207, but collects dequeued nodes. If the sequence length matches the total nodes, the graph is a DAG, return the sorted list, otherwise return empty due to circular deadlock dependencies."},
                    {"id": "269", "name": "Alien Dictionary", "difficulty": "Hard", "key": "DFS Cycle Detection + Reverse Finish Order", "systems_note": "In deep learning compiler instruction schedulers, we infer instruction dependency constraints from adjacent operations. Constructing directed edges and running a topological sort resolves execution priorities."}
                ]
            },
            17: {
                "theme": "Union-Find & Equivalence Classes",
                "problems": [
                    {"id": "261", "name": "Graph Valid Tree", "difficulty": "Medium", "key": "Union-Find Cycle and Connectivity Checks", "systems_note": "Union-Find is the optimal structure for grouping disjoint equivalence classes. An undirected graph is a tree if edges = n-1 and Union-Find finds no cycles (unioning two nodes already in the same root set `find(u) == find(v)` yields a cycle)."},
                    {"id": "323", "name": "Number of Connected Components in an Undirected Graph", "difficulty": "Medium", "key": "Union-Find Component Counter", "systems_note": "Initialize component count to n. For each successful merge of disjoint sets, decrement count by 1. Union-Find with path compression and rank-based unioning executes in near-constant O(1) amortized time per operation."},
                    {"id": "684", "name": "Redundant Connection", "difficulty": "Medium", "key": "Union-Find Cycle Pinpointing", "systems_note": "In redundant network routing path pruning, we locate the final edge that creates a loop. Processing edges sequentially with Union-Find identifies the first cycle-creating edge in O(E) time."}
                ]
            },
            18: {
                "theme": "Prefix Trees (Trie)",
                "problems": [
                    {"id": "208", "name": "Implement Trie (Prefix Tree)", "difficulty": "Medium", "key": "Nested Hash Map Children Nodes", "systems_note": "In Large Language Model (LLM) speculative decoding, serving engines use Tries to index vocabularies, enabling fast prefix constraints validation and KV Cache token matches, drastically reducing sequence comparisons."},
                    {"id": "211", "name": "Design Add and Search Words Data Structure", "difficulty": "Medium", "key": "Trie Wildcard Search via DFS", "systems_note": "Extends standard Trie search with wildcard '.' handling. When encountering '.', we recursively check all child branches of the current node, demonstrating recursive Trie search patterns."},
                    {"id": "642", "name": "Design Search Autocomplete System", "difficulty": "Hard", "key": "Trie + Min-Heap Top-K Filter", "systems_note": "Simulating search engine auto-complete. In speculative decoding or prefix tuning, filtering high-frequency predictions based on string prefixes represents a critical performance path."}
                ]
            },
            19: {
                "theme": "Heaps & Priority Schedulers",
                "problems": [
                    {"id": "23", "name": "Merge k Sorted Lists", "difficulty": "Hard", "key": "Min-Heap Node Tracking / Divide & Conquer", "systems_note": "In distributed stream mergers or log consolidation engines, a min-heap tracks the current head of k sorted streams. This runs in O(N log k) time and represents a core scheduling technique in database log mergers."},
                    {"id": "347", "name": "Top K Frequent Elements", "difficulty": "Medium", "key": "Hash Map + Bucket Sort (O(N) Optimal)", "systems_note": "While a min-heap gives O(N log K), the optimal solution uses bucket sort. Because frequencies are bounded by `[0, N]`, bucket sorting allows linear O(N) retrieval, highlighting a data-driven system optimization choice."},
                    {"id": "295", "name": "Find Median from Data Stream", "difficulty": "Hard", "key": "Dual Balanced Heaps (Max & Min)", "systems_note": "In MLSys runtime telemetry modules, we must compute the median inference latency in O(1) time while accepting new data points in O(log N) time. This is solved by balancing a Max-Heap (smaller values) and a Min-Heap (larger values)."}
                ]
            },
            20: {
                "theme": "Bit Manipulation & Lower-Precision Formats",
                "problems": [
                    {"id": "136", "name": "Single Number", "difficulty": "Easy", "key": "Bitwise XOR properties (a ^ a = 0)", "systems_note": "XOR properties (`x ^ x = 0`, `x ^ 0 = x`) and associativity allow O(N) scan in O(1) space. This is a common parity check and data validation technique in hardware-constrained embedded applications."},
                    {"id": "338", "name": "Counting Bits", "difficulty": "Easy", "key": "DP Bitwise Recurrence", "systems_note": "Using `dp[i] = dp[i >> 1] + (i & 1)` computes set bits for all numbers from 0 to N in O(N) time. Used in quantized weights bitwidth profiling for Binary Neural Networks (BNNs) and INT8 model quantization."},
                    {"id": "190", "name": "Reverse Bits", "difficulty": "Easy", "key": "Bitwise Shifts & Accumulation", "systems_note": "Bitwise swaps. Required for network packet conversions (Big-endian to Little-endian byte order transformations) and graphics pixel bit alignment."},
                    {"id": "137", "name": "Single Number II", "difficulty": "Medium", "key": "Bit-position Modulo Arithmetic", "systems_note": "Simulating logic gates in hardware accelerators (ASICs/FPGAs) or SIMD vector optimizations to track duplicate cycles without using general registers."}
                ]
            },
            21: {
                "theme": "Cache System Implementation",
                "problems": [
                    {"id": "146", "name": "LRU Cache", "difficulty": "Medium", "key": "Hash Map + Doubly Linked List (O(1))", "systems_note": "A primary MLSys design challenge. LRU page eviction is the default mechanism for LLM KV Cache paging (e.g. vLLM's PagedAttention) and deep learning Parameter Server weight swapping. You must hand-code it in O(1) time using a hash map and a doubly linked list. Often extended to discuss thread safety via shared reader-writer locks (shared_mutex) or fine-grained bucket locks in concurrent implementations."},
                    {"id": "460", "name": "LFU Cache", "difficulty": "Hard", "key": "Double Hash Maps + Frequency Lists", "systems_note": "Hard cache eviction. Evicts the least frequently used node, breaking ties using LRU. Requires maintaining a `min_freq` integer and a mapping of frequencies to doubly linked lists, challenging data structure composition skills."},
                    {"id": "622", "name": "Design Circular Queue", "difficulty": "Medium", "key": "Circular Array Modulo Arithmetic", "systems_note": "Ring buffers are the standard data structures for OS IPC (Inter-Process Communication), producer-consumer loops, and GPU command queues. Modulo index updates `(tail + 1) % size` enable lock-free concurrent ring buffer queues."}
                ]
            }
        }
    },
    {
        "name": "Phase 4: Dynamic Programming & High-Pressure Mock (Days 22-30)",
        "target": "Master 1D/2D state transitions, apply space compression optimizations, and practice solving unseen tasks under strict time-box constraints.",
        "days": {
            22: {
                "theme": "1D Dynamic Programming",
                "problems": [
                    {"id": "70", "name": "Climbing Stairs", "difficulty": "Easy", "key": "1D Recurrence + Space Compression", "systems_note": "Basic dynamic programming. Rolling variables `a, b = b, a + b` compress space from O(N) to O(1). In MLSys tensor compilers, minimizing memory footprint via buffer reuse is a key optimization goal."},
                    {"id": "746", "name": "Min Cost Climbing Stairs", "difficulty": "Easy", "key": "Weighted 1D DP Recurrence", "systems_note": "DP recurrence `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`. Can be optimized to O(1) space, helping to build basic dynamic programming muscle memory."},
                    {"id": "322", "name": "Coin Change", "difficulty": "Medium", "key": "Unbounded Knapsack - Bottom-Up DP", "systems_note": "Optimization problem where greedy choices fail. Transition equation: `dp[i] = min(dp[i], dp[i - coin] + 1)`. In runtime system resource scheduler budget allocations, knapsack allocation models are widely applied."}
                ]
            },
            23: {
                "theme": "Subsequences & Knapsack DP",
                "problems": [
                    {"id": "300", "name": "Longest Increasing Subsequence", "difficulty": "Medium", "key": "Patience Sorting / Greedy + Binary Search", "systems_note": "Optimal O(N log N) using greedy tail replacements and binary search. In compiler instruction pipelining, identifying longest non-dependent instruction sequences dictates parallel execution schedules."},
                    {"id": "139", "name": "Word Break", "difficulty": "Medium", "key": "Prefix Partitioning DP + Hash Set", "systems_note": "Evaluating segmentations of contiguous streams. Transition: `dp[i] = any(dp[j] and s[j:i] in wordSet for j in range(i))`. In compiler lexical parsing and token segmentations, prefix partitioning plays a central role."},
                    {"id": "416", "name": "Partition Equal Subset Sum", "difficulty": "Medium", "key": "0-1 Knapsack with Space Compression", "systems_note": "Classic 0-1 knapsack. To compress space, we update a 1D DP array backwards (from right to left) to prevent using values updated in the current iteration, dropping space from O(target) to O(target)."}
                ]
            },
            24: {
                "theme": "2D Grid Dynamic Programming",
                "problems": [
                    {"id": "62", "name": "Unique Paths", "difficulty": "Medium", "key": "Grid DP + Row Rolling Compression", "systems_note": "Grid routing. Transition: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`. In Network-on-Chip (NoC) hardware routing designs, analyzing packet routing paths matches this model. Space can be compressed to a 1D row array."},
                    {"id": "1143", "name": "Longest Common Subsequence", "difficulty": "Medium", "key": "2D Alignment DP Matrix", "systems_note": "LCS is the core algorithm for compiler code-diff checkers and structural network similarity evaluations. Time complexity is O(M*N), and rolling row array updates are often asked in system memory optimization rounds."},
                    {"id": "72", "name": "Edit Distance", "difficulty": "Hard", "key": "2D Match Decision Matrix", "systems_note": "Minimum edit cost calculation. Analyzing state transitions from three cells `dp[i-1][j]`, `dp[i][j-1]`, and `dp[i-1][j-1]` evaluates comprehensive 2D dynamic programming logic."}
                ]
            },
            25: {
                "theme": "Interval & Tree DP",
                "problems": [
                    {"id": "96", "name": "Unique Binary Search Trees", "difficulty": "Medium", "key": "Catalan Number Recurrence", "systems_note": "Counting possible BST shapes. Summing the product of left and right child permutations derives the Catalan recurrence, showcasing algebraic state symmetry."},
                    {"id": "337", "name": "House Robber III", "difficulty": "Medium", "key": "Tree DP + State Tuple DFS Propagation", "systems_note": "In computational graph kernel fusions, selecting optimal operator combinations where adjacent nodes cannot be fused matches tree DP. DFS returns a tuple `(fuse, skip)`, constraining time complexity to O(N)."},
                    {"id": "312", "name": "Burst Balloons", "difficulty": "Hard", "key": "Interval DP (Bottom-Up)", "systems_note": "Advanced interval DP. Reversing the problem to identify 'which balloon is popped last' separates the interval into independent segments, defining the state transition. Crucial for complex compiler scheduler optimizations."}
                ]
            },
            26: {
                "theme": "Greedy Algorithms",
                "problems": [
                    {"id": "55", "name": "Jump Game", "difficulty": "Medium", "key": "Greedy - Backwards Goal Shifting", "systems_note": "Evaluating if a resource packet can route across nodes with variable reach capabilities. Shifting `goal` backwards from the end runs in O(N) time and O(1) space, which is far superior to standard 1D DP (O(N^2))."},
                    {"id": "134", "name": "Gas Station", "difficulty": "Medium", "key": "Net Sum Check + Greedy Pivot Search", "systems_note": "If total supply exceeds total consumption, a solution must exist. A single scan shifts the starting candidate to `i + 1` whenever the rolling sum drops below 0, optimizing the O(N^2) search to O(N)."},
                    {"id": "406", "name": "Queue Reconstruction by Height", "difficulty": "Medium", "key": "Greedy Insertion after Multi-Key Sort", "systems_note": "Scheduling multi-resource allocations with two priorities. Sorting height descending and queue index ascending, then executing index insertions, yields the local queue reconstruction."}
                ]
            },
            27: {
                "theme": "Intervals & Scheduling",
                "problems": [
                    {"id": "56", "name": "Merge Intervals", "difficulty": "Medium", "key": "Sort by Start Time + Linear Merge", "systems_note": "In OS virtual memory managers, when pages are deallocated, contiguous free blocks are coalesced (merged) to minimize memory fragmentation. Coalescing free blocks is logically equivalent to interval merging."},
                    {"id": "435", "name": "Non-overlapping Intervals", "difficulty": "Medium", "key": "Greedy - Sort by End Time", "systems_note": "Classic interval scheduling. To maximize scheduled tasks, prioritize intervals that end earliest. Used in real-time priority task scheduling and instruction pipelines."},
                    {"id": "621", "name": "Task Scheduler", "difficulty": "Medium", "key": "Greedy Bucket Fill with Cooldowns", "systems_note": "In CPU schedulers or GPU thread dispatchers, tasks of the same type must wait for a Cooldown cycle. Estimating cycles by filling buckets with high-frequency tasks resolves the scheduling pattern in O(N) time."}
                ]
            },
            28: {
                "theme": "Mock Simulator Day 1 (Google/Meta Core Systems)",
                "problems": [
                    {"id": "307", "name": "Range Sum Query - Mutable", "difficulty": "Hard", "key": "Segment Tree / Binary Indexed Tree", "systems_note": "In dynamic ML tensors where values are frequently mutated and range sums are queried, prefix sums cost O(N) updates. Segment Trees or Fenwick Trees optimize both operations to O(log N) time, demonstrating query-update balance."},
                    {"id": "588", "name": "Design In-Memory File System", "difficulty": "Hard", "key": "Trie with File Node Directory Tree", "systems_note": "Designing an OS in-memory file system. Models a directory hierarchy using a Trie where terminal nodes represent file contents, supporting `ls`, `mkdir`, `addContentToFile`, and `readContentFromFile` operations."}
                ]
            },
            29: {
                "theme": "Mock Simulator Day 2 (NVIDIA/Apple Hardware & Concurrency)",
                "problems": [
                    {"id": "311", "name": "Sparse Matrix Multiplication", "difficulty": "Medium", "key": "Compressed Row Storage (CRS / CSR) Optimization", "systems_note": "The core kernel of Sparse Neural Networks. In GPU computations, performing dense multiplications on massive zero arrays wastes memory bandwidth. Iterating only over non-zero elements using Row-major formats simulates CSR acceleration hardware kernels."},
                    {"id": "380", "name": "Insert Delete GetRandom O(1)", "difficulty": "Medium", "key": "Hash Map + Dynamic Array Tail Swap", "systems_note": "Used in MLSys negative batch samplers requiring O(1) random draws, inserts, and deletes. A map indexes keys to list offsets. To delete in O(1) time, swap the target element with the last element of the list, then pop back to avoid array shifting."}
                ]
            },
            30: {
                "theme": "Mock Simulator Day 3 (FAANG Hard Graduation Challenges)",
                "problems": [
                    {"id": "460", "name": "LFU Cache", "difficulty": "Hard", "key": "Hand-Code LFU (Review Day 21)", "systems_note": "High-performance cache design under pressure. Evict least-frequently-used nodes, requiring double hash maps and frequency doubly linked list updates in O(1) time."},
                    {"id": "212", "name": "Word Search II", "difficulty": "Hard", "key": "Hand-Code Trie + Backtracking Grid DFS (Review Day 14)", "systems_note": "Integrates Tries, matrix traversals, backtracking, and recursive parent pruning optimizations. Evaluates graph searches and pruning under tight limits."},
                    {"id": "269", "name": "Alien Dictionary", "difficulty": "Hard", "key": "Hand-Code Topological Sort & DFS Cycle Detect (Review Day 16)", "systems_note": "The foundation of compilation pipeline dependencies scheduling. Combines parsing, directed graph construction, cycle validation, and topological sorting."}
                ]
            }
        }
    }
]
