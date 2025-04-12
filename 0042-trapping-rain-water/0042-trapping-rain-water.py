class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n
        maxx = 0
        maxleft = 0
        maxright = 0
        for i in range(n):
            maxleft = max(maxleft, height[i])
            maxL[i] = max(maxleft, height[i])
        for i in range(n-1, -1, -1):
            maxright = max(maxright, height[i])
            maxR[i] = max(maxright, height[i])

        for i in range(n):
            maxx += min(maxL[i], maxR[i]) - height[i]
        return maxx

        