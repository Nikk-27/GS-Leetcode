class TimeMap:                                          # TC: O(LogN)

    def __init__(self):
        self.multi_value_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.multi_value_dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        v = self.multi_value_dict.get(key, [])
        low = 0
        high = len(v) - 1
        return_value = ""

        while low <= high:
            mid = low + (high - low) // 2
            if v[mid][1] <= timestamp:
                return_value = v[mid][0]
                low = mid + 1
            elif v[mid][1] == timestamp:
                return_value = v[mid][0]
            else:
                high = mid - 1
            
        return return_value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)