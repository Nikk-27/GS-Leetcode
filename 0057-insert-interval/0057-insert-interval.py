class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        result.append(intervals[0])
        l = 0
        r = n-1
        if not intervals:
           return [newInterval]

        while l <= r:
            mid = l + (r-l) // 2
            if intervals[mid][0] < newInterval[0]:
                l = mid + 1
            else: r = mid - 1

         # Insert newInterval at the found position    
        intervals.insert(l, newInterval) #O(n)

        # Merge overlapping intervals
        res = []
        for interval in intervals:
            # If res is empty or there is no overlap, add the interval to the result
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # If there is an overlap, merge the intervals by updating the end of the last interval in res
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

# TC = O(n + log n) = O(n)
# SC = O(n)