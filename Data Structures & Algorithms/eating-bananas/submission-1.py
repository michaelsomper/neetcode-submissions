import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k):
            return sum(math.ceil(pile / k) for pile in piles)

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= h:
                hi = mid       # mid works, try to go smaller
            else:
                lo = mid + 1   # mid too slow, need bigger k
        return lo