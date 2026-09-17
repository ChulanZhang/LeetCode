class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = {')': '(', '}': '{', ']': '['}
        for p in s:
            if p in p_map:
                top_p = stack.pop() if stack else '#'
                if p_map[p] != top_p:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0


        # if len(s) % 2 != 0:
        #     return False
        # stack = []
        # for p in s:
        #     if p in ['(', '{', '[']:
        #         stack.append(p)
        #     else:
        #         if p == ')':
        #             if stack and stack[-1] == '(':
        #                 stack.pop()
        #             else:
        #                 return False
        #         elif p == '}':
        #             if stack and stack[-1] == '{':
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             if stack and stack[-1] == '[':
        #                 stack.pop()
        #             else:
        #                 return False
        # return len(stack) == 0
        