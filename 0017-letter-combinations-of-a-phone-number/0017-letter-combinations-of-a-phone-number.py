class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keymap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        results = []

        def backtrack(index, curr_string):
            if len(curr_string) == len(digits):
                results.append(''.join(curr_string))
                return
            possible_letters = keymap[digits[index]]
            for letter in possible_letters:
                curr_string.append(letter)
                backtrack(index + 1, curr_string)
                curr_string.pop()
        backtrack(0, [])

        return results
        