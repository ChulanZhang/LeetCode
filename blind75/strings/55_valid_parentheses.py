from typing import List, Optional, Dict, Set

# LeetCode 20: Valid Parentheses - Easy
# 🔗 Link: https://leetcode.com/problems/valid-parentheses/
# 🔑 Key Points: Stack Data Structure - LIFO
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     Parentheses matching follows a Last-In, First-Out (LIFO) pattern. The most recently opened bracket must be the first one closed. This matches the properties of a stack.
#   - Mathematical Derivation: 
#     1. Initialize an empty stack `stack` and a hash map `mapping` mapping closing brackets to their corresponding opening brackets: `mapping = {')': '(', '}': '{', ']': '['}`.
#     2. Traverse each character `char` in the string:
#        - If `char` is a closing bracket (in `mapping` keys):
#          - Pop the top element from the stack (or use a placeholder like `'#'` if empty). If the popped element does not match the mapped opening bracket, return False.
#        - If `char` is an opening bracket, push it onto the stack.
#     3. After checking the string, return True if the stack is empty (all brackets matched), otherwise False.

class Solution:
    def isValid(self, s: str) -> bool:
        # Time Complexity: O(N) - Single pass traversal. Push and pop operations are O(1)
        # Space Complexity: O(N) - In the worst case (e.g. all opening brackets), stack stores all characters
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            # If it's a closing bracket, validate against the top of the stack
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push onto stack
                stack.append(char)
                
        # Return True only if all opening brackets have been matched and popped
        return not stack

