from typing import List, Optional, Dict, Set

# Group Anagrams (字母异位词分组) - Medium
# 🔑 核心考点: 哈希映射 (Hash Map) / 字符排序键值规范化
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：要把彼此为异位词的字符串分在同一组。我们需要为所有的字母异位词找到一个**共同且唯一的“标识键”（Signature）**，然后以这个标识键作为哈希表的 Key，把原始字符串归纳到同一组中。
#   - 思维推导: 
#     如何设计唯一的“标识键”？
#     1. **方法一：排序**。对于每个字符串，将其字符按字典序排序。例如对 'eat'、'tea' 和 'ate' 排序后都是 'aet'。我们可以将 `'aet'` 作为 Key。排序对于每个长度为 $L$ 的单词耗时 $O(L \\log L)$。
#     2. **方法二：频数统计**。因为只包含小写字母，我们可以用一个长度为 26 的元组记录字符出现的次数，如 `(1, 0, 0, ..., 1, ...)`。元组是可哈希的（immutable），可以作为字典的键。这种方法耗时 $O(L)$。一般面试中排序法已经足够快且更易实现。

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        时间复杂度: O(N * L log L) - N 为字符串列表大小，L 为字符串的最大长度
        空间复杂度: O(N * L) - 哈希表存储所有单词所需要的内存空间
        """
        # 键：排序后的字符串，值：满足该排序形式的所有原始字符串组成的列表
        anagrams_map = {}
        
        for s in strs:
            # 规范化键值：将单词排序，转为元组或字符串作为哈希表的 Key
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams_map:
                anagrams_map[sorted_s] = []
            anagrams_map[sorted_s].append(s)
            
        return list(anagrams_map.values())

