# String category data
PROBLEMS = {
    "50_longest_substring_without_repeating_characters.py": {
        "title": "Longest Substring Without Repeating Characters (无重复字符的最长子串)",
        "difficulty": "Medium",
        "key_points": "滑动窗口 (Sliding Window) / 哈希集合 (Hash Set)",
        "analysis_intuition": "直觉：我们需要在一个字符串中找到一个最长的连续子区间，该区间内的所有字符都是唯一的。使用双重循环遍历所有子串再进行判定会耗费 O(N^2) 时间。为了将复杂度降为 O(N)，我们使用双指针滑动窗口。",
        "analysis_derivation": "滑动窗口原理：\n我们维护一个左指针 `left` 和右指针 `right`，定义它们之间的区间为滑动窗口。我们使用一个哈希集合 `char_set` 存储窗口内的所有字符。\n1. `right` 逐个字符向右移动，扩张窗口。\n2. **冲突收缩**：每当要将字符 `s[right]` 加入窗口时，如果该字符已经在 `char_set` 中，说明窗口内产生了重复字符。此时，我们必须将 `left` 指针向右移动，并同步在 `char_set` 中删除 `s[left]`，直到冲突的那个重复字符被移出窗口。\n3. **窗口合法**：在移除冲突字符后，我们将当前的 `s[right]` 插入集合，并统计当前有效窗口的长度 `right - left + 1`，用其更新最大长度 `max_len`。\n这样每个字符最多只被加入和移出窗口一次，时间复杂度为严格的 O(N)。",
        "code": """class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        \"\"\"
        时间复杂度: O(N) - 左右指针分别最多扫描字符串一次
        空间复杂度: O(min(M, N)) - M 为字符集的大小，N 为字符串的长度
        \"\"\"
        char_set = set()
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 如果新加入的字符已存在，从左侧收缩窗口直到冲突字符被移出
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # 将当前字符加入窗口
            char_set.add(s[right])
            # 更新最大无重复子串长度
            max_len = max(max_len, right - left + 1)
            
        return max_len
"""
    },
    "51_longest_repeating_character_replacement.py": {
        "title": "Longest Repeating Character Replacement (替换后的最长重复字符)",
        "difficulty": "Medium",
        "key_points": "滑动窗口 / 双指针 / 局部频数统计优化",
        "analysis_intuition": "直觉：我们要找一个最长子串，该子串通过替换不超过 k 个字符后可以全部变成同一个字符。如果窗口大小为 `L`，且窗口中出现频率最高的字符次数为 `max_freq`，那么要让这个窗口内字符全部相同，需要替换的字符数就是 `L - max_freq`。只要 `L - max_freq <= k`，这个窗口就是可行的。",
        "analysis_derivation": "使用滑动窗口进行优化：\n1. 初始化 `left = 0`，最大频率记录 `max_freq = 0`，以及一个记录窗口内字符频数的哈希表/数组 `count`。\n2. 遍历右指针 `right`：\n   - 更新当前字符 `s[right]` 的频数：`count[s[right]] += 1`。\n   - 更新窗口内的最大字符频数：`max_freq = max(max_freq, count[s[right]])`。\n   - **收缩条件**：如果当前窗口长度减去最大频数大于 k（即 `(right - left + 1) - max_freq > k`），说明即使把所有非最频字符都替换掉，也无法在 k 次内达到全部相同。此时我们必须收缩窗口：将 `left` 对应字符频数减 1，并向右移动 `left` 指针。\n   - 为什么不需要在收缩窗口时重新计算真正的 `max_freq` 最小值？因为我们只想找更长的子串。当窗口变小时，`max_freq` 的变小不会帮助我们找到比目前历史记录更大的最长子串，所以我们在收缩时保持 `max_freq` 不变也是正确且安全的。\n3. 记录窗口历史最大长度并返回。",
        "code": """class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        \"\"\"
        时间复杂度: O(N) - N 为字符串的长度，每个字符最多被扫描两次
        空间复杂度: O(1) - 仅需大小为 26 的频数哈希表/数组
        \"\"\"
        count = {}
        max_freq = 0
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 累加当前字符频数
            count[s[right]] = count.get(s[right], 0) + 1
            # 维护窗口内的历史最大频数
            max_freq = max(max_freq, count[s[right]])
            
            # 如果需要替换的字符个数超过 k，收缩左指针
            # 窗口宽度为 right - left + 1
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
"""
    },
    "52_minimum_window_substring.py": {
        "title": "Minimum Window Substring (最小覆盖子串)",
        "difficulty": "Hard",
        "key_points": "滑动窗口 / 双哈希计数表 / 双指针最优收缩",
        "analysis_intuition": "直觉：要在 `s` 中找到包含 `t` 中所有字符的最小子串。我们可以先用滑动窗口右指针向右扩展找到一个包含所有 `t` 字符的“可行解”，然后左指针向右收缩，抛弃多余字符，直到窗口刚好不能覆盖 `t`，从而寻找局部最优解。",
        "analysis_derivation": "1. **初始化**：用哈希表 `need` 统计 `t` 中所有字符的出现频数，`required` 为 `t` 中不重复字符的总数。哈希表 `window` 记录当前窗口内满足 `t` 所需字符的频数，变量 `have` 表示窗口中已达到 `need` 频数要求的字符数。\n2. **滑动窗口扩张**：移动右指针 `right`，将 `s[right]` 加进 `window`：\n   - 如果 `s[right]` 在 `need` 中，且 `window[s[right]] == need[s[right]]`，说明该字符数量已达标，令 `have += 1`。\n3. **窗口合法与收缩**：只要 `have == required`，说明窗口已完全覆盖 `t`。我们尝试收缩左侧以寻找更小的窗口：\n   - 记录当前最小长度和子串起点。\n   - 移出左侧字符 `s[left]`，更新 `window`。\n   - 如果移出的 `s[left]` 是必需的且导致频数低于 `need`，更新 `have -= 1`。\n   - 左指针向右移动 `left += 1`。\n4. 遍历完毕后返回历史最小窗口子串，若无则返回 `\"\"`。",
        "code": """class Solution:
    def minWindow(self, s: str, t: str) -> str:
        \"\"\"
        时间复杂度: O(M + N) - M 和 N 分别为字符串 s 和 t 的长度
        空间复杂度: O(M + N) - 两张哈希表占用的辅助空间
        \"\"\"
        if not s or not t:
            return ""
            
        # 统计 t 中字符频数
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
            
        required = len(need)
        window = {}
        have = 0
        
        # 记录最小窗口的长度以及起点、终点索引
        res = float('inf')
        res_indices = [-1, -1]
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # 如果当前字符是所需的，且数量达到了要求
            if char in need and window[char] == need[char]:
                have += 1
                
            # 当窗口满足所有条件时，尝试收缩左指针
            while have == required:
                # 更新历史最小窗口
                if (right - left + 1) < res:
                    res = right - left + 1
                    res_indices = [left, right]
                    
                # 抛弃左边字符
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
                
        l, r = res_indices
        return s[l:r+1] if res != float('inf') else ""
"""
    },
    "53_valid_anagram.py": {
        "title": "Valid Anagram (有效的字母异位词)",
        "difficulty": "Easy",
        "key_points": "哈希计数表 / 字符统计",
        "analysis_intuition": "直觉：字母异位词指的是两个字符串所包含的字母及其出现的频数完全相同，只是顺序不同。我们可以直接统计两个字符串的字符个数进行比对。",
        "analysis_derivation": "1. 快速检查：如果两个字符串的长度不相等，直接返回 `False`。\n2. 使用一个哈希计数表，遍历 `s` 的每个字符令频数加 1，遍历 `t` 的每个字符令频数减 1。\n3. 最后遍历哈希表，如果所有字符的频数都为 0，说明它是合法的异位词，返回 `True`；否则返回 `False`。或者直接使用 Python 的 `collections.Counter` 对比，其底层同样是这一原理。",
        "code": """class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        \"\"\"
        时间复杂度: O(N) - 一次遍历统计字符频数
        空间复杂度: O(1) - 字符集为 26 个小写字母，哈希表大小最多为 26，为常数空间
        \"\"\"
        if len(s) != len(t):
            return False
            
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            
        for val in count.values():
            if val != 0:
                return False
                
        return True
"""
    },
    "54_group_anagrams.py": {
        "title": "Group Anagrams (字母异位词分组)",
        "difficulty": "Medium",
        "key_points": "哈希映射 (Hash Map) / 字符排序键值规范化",
        "analysis_intuition": "直觉：要把彼此为异位词的字符串分在同一组。我们需要为所有的字母异位词找到一个**共同且唯一的“标识键”（Signature）**，然后以这个标识键作为哈希表的 Key，把原始字符串归纳到同一组中。",
        "analysis_derivation": "如何设计唯一的“标识键”？\n1. **方法一：排序**。对于每个字符串，将其字符按字典序排序。例如对 'eat'、'tea' 和 'ate' 排序后都是 'aet'。我们可以将 `'aet'` 作为 Key。排序对于每个长度为 $L$ 的单词耗时 $O(L \\\\log L)$。\n2. **方法二：频数统计**。因为只包含小写字母，我们可以用一个长度为 26 的元组记录字符出现的次数，如 `(1, 0, 0, ..., 1, ...)`。元组是可哈希的（immutable），可以作为字典的键。这种方法耗时 $O(L)$。一般面试中排序法已经足够快且更易实现。",
        "code": """from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        \"\"\"
        时间复杂度: O(N * L log L) - N 为字符串列表大小，L 为字符串的最大长度
        空间复杂度: O(N * L) - 哈希表存储所有单词所需要的内存空间
        \"\"\"
        # 键：排序后的字符串，值：满足该排序形式的所有原始字符串组成的列表
        anagrams_map = {}
        
        for s in strs:
            # 规范化键值：将单词排序，转为元组或字符串作为哈希表的 Key
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams_map:
                anagrams_map[sorted_s] = []
            anagrams_map[sorted_s].append(s)
            
        return list(anagrams_map.values())
"""
    },
    "55_valid_parentheses.py": {
        "title": "Valid Parentheses (有效的括号)",
        "difficulty": "Easy",
        "key_points": "数据结构 - 栈 (Stack) / 先进后出 (LIFO)",
        "analysis_intuition": "直觉：括号匹配具有对称和“就近消除”的特性。最后一个开括号应当最先匹配到闭括号。这完全契合**栈（Stack）**先进后出的数据结构性质。",
        "analysis_derivation": "1. 声明一个空栈 `stack`，以及一个映射字典 `mapping = {')': '(', '}': '{', ']': '['}` 用于检验匹配。\n2. 遍历字符串中的每一个括号 `char`：\n   - 如果 `char` 是一个闭括号（即在字典的 Key 中）：\n     - 弹出栈顶元素。如果栈为空，或者弹出的字符不等于这个闭括号对应的开括号，说明不匹配，返回 `False`。\n   - 如果 `char` 是一个开括号，将其压入栈中。\n3. 遍历结束之后，检查栈是否为空。如果栈为空，说明所有括号都成功匹配并消除了，返回 `True`；如果栈不为空，说明还有多余的开括号未匹配，返回 `False`。",
        "code": """class Solution:
    def isValid(self, s: str) -> bool:
        \"\"\"
        时间复杂度: O(N) - 遍历一次字符串，入栈出栈操作均为 O(1)
        空间复杂度: O(N) - 最坏情况下（全为左括号）栈存储全部字符
        \"\"\"
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # 如果是右括号，尝试与栈顶匹配
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # 如果是左括号，压入栈中
                stack.append(char)
                
        return not stack  # 只有当栈清空时，才是有效括号
"""
    },
    "56_valid_palindrome.py": {
        "title": "Valid Palindrome (验证回文串)",
        "difficulty": "Easy",
        "key_points": "双指针 (Two Pointers) / 字符过滤",
        "analysis_intuition": "直觉：先过滤掉所有非字母和数字的字符，将所有大写字母转为小写。然后检查新字符串是否与其翻转后的字符串相同。但这需要 $O(N)$ 的额外空间。能否实现 $O(1)$ 的空间复杂度？",
        "analysis_derivation": "双指针原地比较破局：\n我们可以在原字符串上使用首尾双指针 `left` 和 `right`：\n1. 初始化 `left = 0`，`right = len(s) - 1`。\n2. 在 `left < right` 的循环中：\n   - 如果 `s[left]` 不是字母或数字，右移：`left += 1`，跳过该字符。\n   - 如果 `s[right]` 不是字母或数字，左移：`right -= 1`，跳过该字符。\n   - 如果两个指针指向的都是合法字符，转换为小写字母比对。若不相等，判定不是回文，直接返回 `False`。\n   - 若相等，双指针相向移动一步：`left += 1`，`right -= 1`。\n3. 顺利走完循环说明是有效回文串，返回 `True`。无需分配额外空间。",
        "code": """class Solution:
    def isPalindrome(self, s: str) -> bool:
        \"\"\"
        时间复杂度: O(N) - 每个字符最多被两个指针扫描一次
        空间复杂度: O(1) - 原地双指针移动，无额外开销
        \"\"\"
        left, right = 0, len(s) - 1
        
        while left < right:
            # 过滤左侧非字母数字的字符
            while left < right and not s[left].isalnum():
                left += 1
            # 过滤右侧非字母数字的字符
            while left < right and not s[right].isalnum():
                right -= 1
                
            # 比较是否相等（忽略大小写）
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
"""
    },
    "57_longest_palindromic_substring.py": {
        "title": "Longest Palindromic Substring (最长回文子串)",
        "difficulty": "Medium",
        "key_points": "中心扩散法 (Expand Around Center) / 动态规划",
        "analysis_intuition": "直觉：如果使用暴力枚举，找到所有可能的子串并判定是不是回文，需要 O(N^3) 的复杂度。即使使用普通的 2D 动态规划，空间和时间也均为 O(N^2)。我们需要更优的方案。",
        "analysis_derivation": "中心扩散法（极佳的 O(1) 空间方案）推导：\n回文串具有高度的中心对称性。我们可以尝试**以每个位置作为回文中心，向两边扩散**来寻找最长回文串：\n1. 遍历字符串中的每一个字符索引 `i`。\n2. **奇数长度回文**：以当前字符 `s[i]` 为中心，向两侧扩散（即左右指针初始为 `(i, i)`）。\n3. **偶数长度回文**：以两个相邻字符 `s[i]` 和 `s[i+1]` 之间的空隙为中心，向两侧扩散（即左右指针初始为 `(i, i+1)`）。\n4. 扩散逻辑：如果 `left >= 0` 且 `right < len(s)` 且两端字符相同 `s[left] == s[right]`，则继续扩散：`left -= 1`, `right += 1`。直到不满足条件。此时回文子串为 `s[left+1:right]`。我们统计并记录最长的回文子串。由于只有 2n-1 个可能的中心，总时间复杂度为 O(N^2)，空间为 O(1)。",
        "code": """class Solution:
    def longestPalindrome(self, s: str) -> str:
        \"\"\"
        时间复杂度: O(N^2) - 每个中心扩散最多需要 O(N) 步，共有 2N-1 个中心
        空间复杂度: O(1) - 仅需存储几个指针和边界变量
        \"\"\"
        if not s or len(s) < 1:
            return ""
            
        res = ""
        
        # 辅助扩散函数，返回以此为中心的最长回文子串
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
            
        for i in range(len(s)):
            # 奇数长度回文 (如 "aba")
            p1 = expand(i, i)
            # 偶数长度回文 (如 "abba")
            p2 = expand(i, i + 1)
            
            # 更新全局最长回文子串
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
                
        return res
"""
    },
    "58_palindromic_substrings.py": {
        "title": "Palindromic Substrings (回文子串个数)",
        "difficulty": "Medium",
        "key_points": "中心扩散法 (Expand Around Center) / 回文计数",
        "analysis_intuition": "直觉：这道题需要统计字符串中所有回文子串的个数。既然回文子串都是围绕某个中心对称的，我们同样可以采用中心扩散法：每成功向外扩散一步，就说明我们找到了一个新的回文子串，计数器加 1。",
        "analysis_derivation": "与上一题“最长回文子串”类似，我们利用 2N-1 个回文中心进行扩散：\n1. 遍历字符串中的每一个索引 `i`。\n2. **以第 i 个字符为中心**启动扩散：\n   - 初始化 `l = i`, `r = i`。\n   - 循环检查是否满足 `l >= 0` 且 `r < len(s)` 且 `s[l] == s[r]`。只要满足，说明 `s[l:r+1]` 是回文串，计数器 `count += 1`。然后向外扩散 `l -= 1`, `r += 1`。\n3. **以第 i 和第 i+1 个字符为中心**启动扩散：\n   - 初始化 `l = i`, `r = i + 1`。\n   - 执行同样的扩散条件和计数。\n4. 遍历所有中心结束后，累加的总计数即为全部回文子串的数量。空间复杂度仅为 O(1)。",
        "code": """class Solution:
    def countSubstrings(self, s: str) -> int:
        \"\"\"
        时间复杂度: O(N^2) - 每个中心最多扩散 O(N) 步
        空间复杂度: O(1)
        \"\"\"
        count = 0
        n = len(s)
        
        def expand_and_count(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
                
        for i in range(n):
            # 奇数长度中心扩散
            expand_and_count(i, i)
            # 偶数长度中心扩散
            expand_and_count(i, i + 1)
            
        return count
"""
    },
    "59_encode_and_decode_strings.py": {
        "title": "Encode and Decode Strings (字符串的编码与解码)",
        "difficulty": "Medium",
        "key_points": "序列化与反序列化 / 长度前缀协议 (Length-prefixed encoding)",
        "analysis_intuition": "直觉：我们需要将一个字符串列表序列化为一个单一的字符串，之后能完美将其恢复。使用简单的分隔符（如逗号或特殊符号）有很大缺陷——如果原始字符串中本身就包含了该分隔符，解码时就会产生歧义导致切分错误。",
        "analysis_derivation": "采用网络通信协议中经典的**长度前缀编码 (Length-prefixed encoding)** 彻底破局：\n1. **编码 (Encode)**：对于列表中的每个字符串 `s`，我们先计算它的长度 `len(s)`，然后拼上一个非数字的分隔符（比如字符 `'#'`），再拼上原始字符串本身。最终编码为：`[length] + '#' + s`。\n   - 例如：`[\"hello\", \"world\"]` 编码为 `\"5#hello5#world\"`。\n   - 即使原始字符串包含 `#`（例如 `\"ab#c\"`），也会被编码为 `\"4#ab#c\"`，解析时不会有歧义。\n2. **解码 (Decode)**：使用一个遍历指针 `i = 0` 扫描编码后的字符串：\n   - 从位置 `i` 开始往后寻找第一个出现的 `'#'`，将其前面的子串提取出来并转换为整数，这代表了接下来那个字符串的精确长度 `length`。\n   - 跳转过字符 `'#'`，从当前位置提取长度为 `length` 的字符，这就是我们需要的原字符串。\n   - 将提取的字符串存入结果集，并将指针移动到下一个编码块的起点：`i = sharp_index + 1 + length`，重复读取，直到字符串结束。",
        "code": """from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        \"\"\"Encodes a list of strings to a single string.
        \"\"\"
        res = []
        for s in strs:
            # 编码协议：长度 + '#' + 字符串本身
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        \"\"\"Decodes a single string to a list of strings.
        \"\"\"
        res = []
        i = 0
        
        while i < len(s):
            # 寻找当前数据块的长度分隔符 '#'
            sharp_idx = s.find('#', i)
            # 提取长度前缀
            length = int(s[i:sharp_idx])
            # 根据提取出的长度切割出原字符串
            start = sharp_idx + 1
            end = start + length
            res.append(s[start:end])
            # 移动指针处理下一个字符串
            i = end
            
        return res
"""
    }
}
