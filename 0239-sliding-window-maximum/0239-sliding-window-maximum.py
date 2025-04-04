class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

    # monotonic decreasing queue method
    
        deq = deque()

        result = []
        j = 0
        n = len(nums)
        i = 0

        if n == 0:
            return []

        for j in range(n):
            while deq and deq[0] <= j-k:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[j]:
                deq.pop()

            deq.append(j)

            if j >= k-1:
                result.append(nums[deq[0]])

        return result

# TC = O(N)
# SC = O(W) W=number of windows

#         n = len(nums)
#         window = []
#         output = []
#         h = 0
#         i = 0

#         for j in range(n):
#             if h < k:
#                 window.append(nums[j])
#                 h += 1
#                 if h == k:
#                     output.append(max(window))
#                     h -= 1
#                     window.remove(nums[i])
#                     i += 1
#         return output

# # TC = O(N)
# # SC = O(N)

        