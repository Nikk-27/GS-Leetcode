class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        def solve(i, r, c):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROW or c >= COL or board[r][c] == '#' or board[r][c] != word[i]):
                return False
            
            board[r][c] = '#'
            res = (solve(i+1, r+1, c) or 
                    solve(i+1, r-1, c) or
                    solve(i+1, r, c+1) or
                    solve(i+1, r, c-1))
            return res

        for i in range(ROW):
            for j in range(COL):
                if solve(0,i,j):
                    return True
        return False

# Time complexity: O(m * 4^n)
# Space complexity: O(n)
# Where m is the number of cells in the board and n is the length of the word.
# At each character, you recursively try up to 3 directions (up/down/left/right but excluding the direction you just came from to avoid revisiting the previous cell).

# O(3^n) paths per cell × m cells =O(m × 3^n)

# m = row * col

