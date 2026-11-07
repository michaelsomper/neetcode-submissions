class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string;

        size_t total_len = 0;

        for (const string& str : strs) {
            total_len += str.size() + 2;
        }
        encoded_string.reserve(total_len);

        char char_buffer[16];
        for (const string& str : strs) {
            int size = str.length();
            auto [ptr, ec] = std::to_chars(char_buffer, char_buffer + sizeof(char_buffer), size);

            encoded_string.append(char_buffer, ptr - char_buffer);

            encoded_string += '#';
            encoded_string += str;
        }

        return encoded_string;
    }

    vector<string> decode(string s) {
        std::vector<string> strs;
        size_t len = s.size();
        string str;

        int i = 0;      

        while (i < len) {
            string chunk_length;
            while (s[i] != '#') {
                chunk_length += s[i];
                i += 1;
            }

            i += 1;
            int chunk_size = std::stoi(chunk_length);
            str = s.substr(i, chunk_size);
            i += chunk_size;
            strs.push_back(str);
        }

        return strs;
    }
};
