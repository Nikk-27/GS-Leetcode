class Solution:
#  Smart Recursion

    def __init__(self):
        self.result = []
    def solve(self, n, cur, open, close):
        if len(cur) == 2*n:
            self.result.append(''.join(cur))
            return

        if open < n:
            cur.append('(')
            self.solve(n, cur, open+1, close)
            cur.pop()
        if close < open:
            cur.append(')')
            self.solve(n, cur, open, close+1)
            cur.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        cur = []
        self.solve(n, cur, 0, 0)
        return self.result
        

# TC = O(2^2n)  2 options to choose from then 2n correct strings possible
# SC = O(2n)    2n results possible for n