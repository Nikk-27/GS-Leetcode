class Solution:

    def __init__(self, w: List[int]):
        self.sum = [w[0]]
        for i in range(1, len(w)):
            self.sum.append(self.sum[-1] + w[i])
        self.max = self.sum[-1]

    def pickIndex(self) -> int:
        n = len(self.sum)
        l = 0
        r = n-1
        target = random.randint(0, self.max - 1)
        while l < r:
            mid = l + (r-l) // 2
            if self.sum[mid] >= target:
                r = mid
            else:
                l = mid+1
        return l 
        

# TC = O(n) for initialization, O(log n) for selection
# SC = O(n)
# https://www.youtube.com/watch?v=3Ky9ZlI95cY
