class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)

        def b(i, cur):
            if i == n:
                res.append(cur[:])
                return

            cur.append(nums[i])
            b(i+1, cur)
            cur.pop()
            b(i+1, cur)
        b(0, [])
        return res