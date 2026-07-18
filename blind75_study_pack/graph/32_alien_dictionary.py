from typing import List, Optional, Dict, Set

# Alien Dictionary - Hard
# 🔑 Key Points: Topological Sort / Cycle Detection / Directed Graphs
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Given a sorted list of words in an alien language, we need to extract the order of characters. In a dictionary, word ordering is determined by the first differing character. We can build directed edges `c1 -> c2` by comparing adjacent words and then run a topological sort.
#   - Mathematical Derivation: 
#     1. **Graph Construction**: Compare adjacent words `w1` and `w2` character by character. The first mismatch `w1[j] != w2[j]` gives an edge `w1[j] -> w2[j]`. If `w1` is longer than `w2` and `w2` is a prefix of `w1` (e.g., 'abc' comes before 'ab'), this is an invalid order, so we return "".
#     2. **Topological Sort (DFS / BFS)**: Run DFS with three-state coloring (0: unvisited, 1: visiting, 2: visited) to detect cycles. If we encounter a node in state 1 during DFS, there is a cycle, so we return "". If the graph is acyclic, reverse the DFS finish order to get the topological order.

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Time Complexity: O(C) - C is the total length of all words combined
        # Space Complexity: O(V + E) - Adjacency list representation (V <= 26)
        
        # Initialize graph adjacency list
        adj = {char: set() for word in words for char in word}
        
        # 1. Build directed graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # Prefix boundary check: if w1 is longer and has w2 as prefix, order is invalid
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
        # 2. Cycle detection and topological sort using DFS
        visiting = set()  # Set of nodes currently in recursion stack
        visited = set()   # Set of nodes fully processed
        res = []
        
        def dfs(char):
            if char in visiting:
                return False  # Cycle detected
            if char in visited:
                return True
                
            visiting.add(char)
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)  # Append node after exploring all paths from it
            return True
            
        for char in adj:
            if not dfs(char):
                return ""  # Cycle exists, return empty
                
        # Reverse the result list since DFS returns reverse order
        return "".join(res[::-1])

