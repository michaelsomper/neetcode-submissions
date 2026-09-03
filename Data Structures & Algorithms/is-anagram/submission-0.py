class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_dict = {}

        for letter in s:
            try:
                letter_dict[letter] += 1
            except:
                letter_dict[letter] = 1

        for letter in t:
            try:
                letter_dict[letter] -= 1
                if letter_dict[letter] < 0:
                    return False
            except:
                return False

        for key in letter_dict:
            if letter_dict[key] > 0:
                return False
        
        return True
