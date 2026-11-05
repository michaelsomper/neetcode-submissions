class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> letter_map;

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            letter_map[s[i]]++;
            letter_map[t[i]]--;
        }

        for (const auto& [key, value] : letter_map) {
            if (value != 0) {
                return false;
            }
        }

        return true;
    }
};
