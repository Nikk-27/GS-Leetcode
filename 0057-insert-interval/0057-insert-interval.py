class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        i = 0

        while i < n:
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                break
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        result.append(newInterval)
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
        
# TC = O(n)
# SC = O(n)