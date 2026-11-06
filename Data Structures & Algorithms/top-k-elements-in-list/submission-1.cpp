class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        using Pair = std::pair<int, int>;
        std::unordered_map<int, int> num_dict;
        std::priority_queue<Pair, std::vector<Pair>, std::greater<Pair>> min_heap;

        for (int num : nums) {
            num_dict[num]++;
        }

        for (const auto& [key, value] : num_dict) {
            min_heap.push({value, key});
            if (min_heap.size() > k) {
                min_heap.pop();
            }
        }

        std::vector<int> k_largest;
        for (int i = 0; i < k; i++) {
            auto temp = min_heap.top();
            min_heap.pop();
            k_largest.push_back(temp.second);
        }

        return k_largest;
    }
};
