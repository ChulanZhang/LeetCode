from typing import List, Optional, Dict, Set

# Encode and Decode Strings (字符串的编码与解码) - Medium
# 🔑 核心考点: 序列化与反序列化 / 长度前缀协议 (Length-prefixed encoding)
#
# 🧠 深入分析与破局点:
#   - 直觉与陷阱: 
#     直觉：我们需要将一个字符串列表序列化为一个单一的字符串，之后能完美将其恢复。使用简单的分隔符（如逗号或特殊符号）有很大缺陷——如果原始字符串中本身就包含了该分隔符，解码时就会产生歧义导致切分错误。
#   - 思维推导: 
#     采用网络通信协议中经典的**长度前缀编码 (Length-prefixed encoding)** 彻底破局：
#     1. **编码 (Encode)**：对于列表中的每个字符串 `s`，我们先计算它的长度 `len(s)`，然后拼上一个非数字的分隔符（比如字符 `'#'`），再拼上原始字符串本身。最终编码为：`[length] + '#' + s`。
#        - 例如：`["hello", "world"]` 编码为 `"5#hello5#world"`。
#        - 即使原始字符串包含 `#`（例如 `"ab#c"`），也会被编码为 `"4#ab#c"`，解析时不会有歧义。
#     2. **解码 (Decode)**：使用一个遍历指针 `i = 0` 扫描编码后的字符串：
#        - 从位置 `i` 开始往后寻找第一个出现的 `'#'`，将其前面的子串提取出来并转换为整数，这代表了接下来那个字符串的精确长度 `length`。
#        - 跳转过字符 `'#'`，从当前位置提取长度为 `length` 的字符，这就是我们需要的原字符串。
#        - 将提取的字符串存入结果集，并将指针移动到下一个编码块的起点：`i = sharp_index + 1 + length`，重复读取，直到字符串结束。

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            # 编码协议：长度 + '#' + 字符串本身
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
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

