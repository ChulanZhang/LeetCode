class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        results = []
        def backtrack(start, path):
            if start == len(s):
                results.append(path[:])
                return
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return results
        