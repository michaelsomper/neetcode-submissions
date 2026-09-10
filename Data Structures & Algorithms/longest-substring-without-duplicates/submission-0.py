from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left_pointer = 0
        right_pointer = 0

        length = 0
        max_length = 0

        character_window_dict = defaultdict(int)

        while right_pointer < len(s):
            character_window_dict[s[right_pointer]] += 1

            while character_window_dict[s[right_pointer]] > 1:
                character_window_dict[s[left_pointer]] -= 1
                left_pointer += 1
            
            length = right_pointer - left_pointer + 1

            if length > max_length:
                max_length = length

            right_pointer += 1

        return max_length