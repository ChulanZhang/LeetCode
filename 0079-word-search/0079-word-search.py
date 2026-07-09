class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # start from a starting point, define a dfs function
        def dfs(r, c, index):
            # check the boundry first
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            # Check whether current cell matches current character.
            if board[r][c] != word[index]:
                return False
            
                        # If this is the last character and it matches,
            # we have found the word.
            if index == len(word) - 1:
                return True

            # Mark current cell as visited.
            temp = board[r][c]
            board[r][c] = "#"

            # try four directions
            found = (
                dfs(r + 1, c, index + 1) or 
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
             )

            board[r][c] = temp
            return found
        
        # try every cell as the starting point
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
