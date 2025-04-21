class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def findpivot():
            l, r = 0, n - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        pivot = findpivot()
        return nums[pivot]

# TC = O(log n)
# SC = O(1)