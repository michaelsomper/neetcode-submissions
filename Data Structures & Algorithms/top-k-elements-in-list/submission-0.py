import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)

        for num in nums:
            count_dict[num] += 1
        
        heap = []

        for key in count_dict:
            heapq.heappush(heap, (count_dict[key], key))

        n_largest = heapq.nlargest(k, heap)

        topKFrequent = []

        for tup in n_largest:
            topKFrequent.append(tup[1])

        return topKFrequent