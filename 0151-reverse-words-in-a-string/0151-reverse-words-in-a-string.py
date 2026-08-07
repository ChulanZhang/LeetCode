class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_word = reversed(s.split())
        return " ".join(reversed_word)
        