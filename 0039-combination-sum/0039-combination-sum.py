class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        n = len(candidates)
        candidates.sort()

        def b(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i == n or total > target:
                return
            
            cur.append(candidates[i])
            b(i, cur, total+candidates[i])
            cur.pop()

            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
            b(i+1, cur, total)
        
        b(0, [], 0)
        return res

# TC = O(2^n * n)
# SC = O(n)