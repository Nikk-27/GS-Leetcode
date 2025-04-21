class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        def binarysearch(l, r):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        pivot = findpivot()

        if nums[pivot] <= target <= nums[n - 1]:
            return binarysearch(pivot, n - 1)
        else:
            return binarysearch(0, pivot - 1)

# TC = O(log n)
# SC = O(1)
                


                