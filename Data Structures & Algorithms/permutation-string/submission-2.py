from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        s1_counter = Counter(s1)

        for i in range(len(s2) - k + 1):
            print(s2[i:i+k])
            if Counter(s2[i:i+k]) == s1_counter:
                return True
        
        return False