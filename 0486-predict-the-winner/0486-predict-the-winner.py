class Solution:
#  When it's your turn 
#       -> Do your best (max)
#  When it's your opponents turn
#       -> expect the worst from result(min) because he will also take max then you are left with min part

# Optimal game strategy (Min Max Game)

    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(i, j):
            if i > j :
                return 0
            if i == j:
                return nums[i]
            #        P1 first turn + P1 second turn after P2 is done
            take_i = nums[i]       + min(solve(i+2, j), solve(i+1, j-1))
            take_j = nums[j]       + min(solve(i, j-2), solve(i+1, j-1))
            return max(take_i, take_j)

        n = len(nums)
        total = sum(nums) 
        P1 = solve(0, n-1)
        P2 = total - P1
        return P1 > P2


# TC = O(2^n) due to 2 options at every index
# SC = O(n) due to recursion stack