class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def capture(i, j):
            if rows <= i or i < 0 or cols <= j or j < 0 or board[i][j] != 'O':
                return
                board[i][j] = 'T'
                capture(i+1, j)
                capture(i-1, j)
                capture(i, j-1)
                capture(i, j+1)

        # convert border O to T

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and ( i in [0, rows-1] or j in [0, cols-1]):
                    capture(i,j)

        print(board)

        # convert middle O to X

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # convert border T back to O

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
        