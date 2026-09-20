import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        
        for num in stones:
            heapq.heappush(max_heap, -num)

        while len(max_heap) > 1:
            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)

            if a > b:
                a -= b
                heapq.heappush(max_heap, -a)  
        
        if max_heap:
            return -heapq.heappop(max_heap)
        else:
            return 0


