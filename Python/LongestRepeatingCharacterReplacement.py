"""
You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
https://leetcode.com/problems/longest-repeating-character-replacement/description/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        max_frequency = 0
        char_count = {}

        for right in range(len(s)):
            right_element = s[right]
            char_count[right_element] = char_count.get(right_element, 0) + 1
            max_frequency = max(max_frequency, char_count[right_element])
            substring_length = right - left + 1

            while (substring_length - max_frequency) > k:
                left_element = s[left]
                char_count[left_element] -= 1

                if char_count[left_element] == 0:
                    del char_count[left_element]

                left += 1
                substring_length = right - left + 1

            max_length = max(max_length, substring_length)

        return max_length


if __name__ == "__main__":
    solution = Solution()
    # Test case 1: All same characters
    print(solution.characterReplacement("AAAA", 1))  # Expected: 4
    # Test case 2: Example 1 from problem
    print(solution.characterReplacement("ABAB", 2))  # Expected: 4
    # Test case 3: Example 2 from problem
    print(solution.characterReplacement("AABABBA", 1))  # Expected: 4
    # Test case 4: No replacements allowed
    print(solution.characterReplacement("ABCD", 0))  # Expected: 1
    # Test case 5: Single character
    print(solution.characterReplacement("A", 0))  # Expected: 1
    # Test case 6: Large k
    print(solution.characterReplacement("ABCDEF", 10))  # Expected: 6
