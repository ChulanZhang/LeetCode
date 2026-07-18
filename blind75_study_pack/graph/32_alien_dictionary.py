from typing import List, Optional, Dict, Set

# Alien Dictionary (外星人词典) - Hard
# 🔑 核心考点: 拓扑排序 (Topological Sort) / 环路检测 / 字符串对齐比较
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：词典中单词是有序的，我们需要提取出字符之间的优先顺序。例如在英语字典中，'apple' 在 'banana' 之前是因为 'a' 的优先级高于 'b'。因此我们可以通过对比相邻两个单词的字符来构建字符间的有向边，然后跑拓扑排序。
#   - 思维推导: 
#     1. **构建图**：相邻单词 `w1` 和 `w2` 对齐比较，找到第一个不同的字符 `c1` 和 `c2`。说明有一条有向边 `c1 -> c2`。如果出现 `w1` 是 `w2` 的前缀但 `len(w1) > len(w2)`（如 'abc' 在 'ab' 之前），这是非法的，直接返回空字符串。
#     2. **拓扑排序 (DFS 三色标记法/BFS)**：我们用 DFS 检测环路。在 DFS 中，对每个节点使用三种状态标记：0 代表未访问，1 代表正在访问（递归栈中），2 代表已访问。若在搜索中遇到了状态 1 的节点，说明存在环，返回无效。若无环，DFS 退出时将节点压入结果栈，最后逆序输出即为拓扑排序结果。

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        时间复杂度: O(C) - C 为所有单词中字符的总长度，建图和拓扑排序的复杂度均与字符总数呈线性关系
        空间复杂度: O(V + E) - V 为字符种类数（最大为 26），有向图邻接表空间
        """
        # 初始化图的邻接表
        adj = {char: set() for word in words for char in word}
        
        # 1. 比较相邻单词，构建有向图
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # 边界异常检查：如果 w1 长于 w2 且 w2 是 w1 的前缀，说明非法（如 'abc' 排在 'ab' 前面）
            if len(w1) > len(w2) and w1[:min_len] == w2:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
        # 2. DFS 环路检测与拓扑排序
        # visiting 记录正在递归访问的节点（检测环），visited 记录已处理完毕的节点
        visiting = set()
        visited = set()
        res = []
        
        def dfs(char):
            if char in visiting:
                return False  # 发现环路
            if char in visited:
                return True
                
            visiting.add(char)
            for neighbor in adj[char]:
                if not dfs(neighbor):
                    return False
            visiting.remove(char)
            visited.add(char)
            res.append(char)
            return True
            
        # 遍历图的所有节点跑 DFS
        for char in adj:
            if not dfs(char):
                return ""
                
        # 因为 DFS 在退出时才将节点入栈，所以拓扑排序结果需要反转
        return "".join(res[::-1])

