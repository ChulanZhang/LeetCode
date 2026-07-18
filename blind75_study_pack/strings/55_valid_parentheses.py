from typing import List, Optional, Dict, Set

# Valid Parentheses (有效的括号) - Easy
# 🔑 核心考点: 数据结构 - 栈 (Stack) / 先进后出 (LIFO)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：括号匹配具有对称和“就近消除”的特性。最后一个开括号应当最先匹配到闭括号。这完全契合**栈（Stack）**先进后出的数据结构性质。
#   - 思维推导: 
#     1. 声明一个空栈 `stack`，以及一个映射字典 `mapping = {')': '(', '}': '{', ']': '['}` 用于检验匹配。
#     2. 遍历字符串中的每一个括号 `char`：
#        - 如果 `char` 是一个闭括号（即在字典的 Key 中）：
#          - 弹出栈顶元素。如果栈为空，或者弹出的字符不等于这个闭括号对应的开括号，说明不匹配，返回 `False`。
#        - 如果 `char` 是一个开括号，将其压入栈中。
#     3. 遍历结束之后，检查栈是否为空。如果栈为空，说明所有括号都成功匹配并消除了，返回 `True`；如果栈不为空，说明还有多余的开括号未匹配，返回 `False`。

class Solution:
    def isValid(self, s: str) -> bool:
        """
        时间复杂度: O(N) - 遍历一次字符串，入栈出栈操作均为 O(1)
        空间复杂度: O(N) - 最坏情况下（全为左括号）栈存储全部字符
        """
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

