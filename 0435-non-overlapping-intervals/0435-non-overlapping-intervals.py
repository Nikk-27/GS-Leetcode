class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()  # Sort by start time
        count = 0
        last_interval = intervals[0]
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            last_end = last_interval[1]

            if curr_start >= last_end:
                last_interval = intervals[i]  # Safe to keep
            elif curr_end >= last_end:
                count += 1  # Remove current interval
            else:
                last_interval = intervals[i]  # Replace with current (greedy choice)
                count += 1
        
        return count

# TC = O(n log n)
# SC = O(1)
