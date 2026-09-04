from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = defaultdict(list)

        for string in strs:
            sorted_string = "".join(sorted(string))
            sorted_strings[sorted_string].append(string)

        grouped = []

        for key in sorted_strings:
            group = sorted_strings[key]
            grouped.append(group)

        return grouped
        
        