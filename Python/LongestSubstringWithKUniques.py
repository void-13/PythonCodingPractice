# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.
# https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

# Time Complexity: O(n)
# Space Complexity: O(min(n, k))


def longest_k_substr(s, k):
    if not s or k <= 0:
        return -1

    left = max_len = 0
    char_map = {}

    for right in range(len(s)):
        char_map[s[right]] = char_map.get(s[right], 0) + 1

        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1

        if len(char_map) == k:
            max_len = max(max_len, right - left + 1)

    return max_len if max_len > 0 else -1


print(longest_k_substr("aabaaab", 2))
print(longest_k_substr("aaaa", 1))
print(longest_k_substr("abc", 2))
print(longest_k_substr("abc", 5))
