class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom up method
        maxi = 1
        t = [1] * (len(nums))

        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    t[i] = max(t[i], 1 + t[j])
                    maxi = max(maxi, t[i])
        return maxi

# TC = O(n^2)
# SC = O(n)