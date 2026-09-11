from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if self.time_map[key]:
            left, right = 0, len(self.time_map[key]) - 1

            while left <= right:
                mid = (left + right) // 2
                if self.time_map[key][mid][1] == timestamp:
                    return self.time_map[key][mid][0]
                if self.time_map[key][mid][1] < timestamp:
                    left = mid + 1
                else:
                    right = mid - 1
            
            mid = (right + left) // 2
                
            if self.time_map[key][mid][1] > timestamp:
                return ""
            
            return self.time_map[key][mid][0]
        
        return ""
