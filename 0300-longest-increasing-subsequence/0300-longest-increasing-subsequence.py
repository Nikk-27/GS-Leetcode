class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # whenever subsequence asked we use take/ skip method

        self.n = len(nums)
        dp = [[-1] * (self.n+1) for _ in range(self.n)]
        self.nums = nums

        def solve(cur, prev):
            take = 0
            skip = 0

            if cur == self.n:
                return 0

            if dp[cur][prev] != -1: return dp[cur][prev]

            if prev == -1 or self.nums[prev] < self.nums[cur]:
                take = 1 + solve(cur+1, cur)
            
            skip = solve(cur+1, prev)
            dp[cur][prev] = max(take, skip)

            return dp[cur][prev]

        return(solve(0, -1))
        

# Time: O(N^2) due to memoization table of size N x (N+1)
# Space: O(N^2) for the DP array (dp[][]) + recursion stack up to O(N)

# TC = O(2^N) without memoization because for each position we have 2 options
# SC = O(N) without memoization (just the recursion stack)