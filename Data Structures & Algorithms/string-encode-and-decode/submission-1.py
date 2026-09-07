class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            len_str = ""
            if len(strs[i]) < 10:
                len_str = "00" + str(len(strs[i]))
            elif len(strs[i]) < 100:
                len_str = "0" + str(len(strs[i]))
            else:
                len_str = str(len(strs[i]))
                
            strs[i] = len_str + strs[i]
        
        encoded_string = "".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        str_list = []

        while i < len(s):
            length = int(s[i:i+3])
            i += 3
            new_string = s[i:i+length]
            str_list.append(new_string)
            i += length

        return str_list
                



