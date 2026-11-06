class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<string, vector<string>> str_dict;

        for (int i = 0; i < strs.size(); i++) {
            string sorted_str = strs[i];
            std::sort(sorted_str.begin(), sorted_str.end());
            str_dict[sorted_str].push_back(strs[i]);
        }

        std::vector<std::vector<string>> grouped_strs;
        for (const auto& [key, values] : str_dict) {
            grouped_strs.push_back(std::move(values));
        }

        return grouped_strs;
    }
};
