class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = sorted(nums)
        self.index = len(nums) - k

    def add(self, val: int) -> int:
        left = 0
        right = len(self.stream) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.stream[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        
        self.index += 1
        self.stream.insert(left, val)    

        return self.stream[self.index] 
