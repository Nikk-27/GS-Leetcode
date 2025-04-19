class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur = []
        res = []
        n = len(s)

        def ispalindrome(ss):
            l = 0
            r = len(ss) - 1
            while l <= r:
                if ss[l] != ss[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        def backtrack(idx, cur, res):
            if idx == n:
                res.append(cur.copy())
                return
            
            for i in range(idx, n):
                print(s[idx:i+1])
                if ispalindrome(s[idx:i+1]):
                    cur.append(s[idx:i+1])
                    backtrack(i+1, cur, res)
                    cur.pop()
        backtrack(0, cur, res)
        return res

# TC = O(2^n) * O(n) // at each position in s we have 2 choices so total 2^n choices and then O(n) for the palindrome check
# SC = O(n) // recursion stack