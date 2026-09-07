class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_sequence_len = 0

        for num in nums_set:
            if (num - 1) in nums_set:
                continue
            else:
                length = 1
                current_num = num
                while (current_num + 1) in nums_set:
                    length += 1
                    current_num += 1

                if length > longest_sequence_len:
                    longest_sequence_len = length
        
        return longest_sequence_len