class Solution:
    def hammingWeight(self, n: int) -> int:
        string_n = bin(n)
        num_ones = 0
        for c in string_n:

            if c == '1':
                num_ones += 1
        return num_ones