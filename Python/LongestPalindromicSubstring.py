"""
Given a string s, return the longest palindromic substring in s.
https://leetcode.com/problems/longest-palindromic-substring/description/?envType=problem-list-v2&envId=two-pointers
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach: Expand Around Centers
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        if not s or len(s) <= 1:
            return s

        start = 0
        max_length = 0

        for current in range(len(s)):
            # Check odd-length palindrome (single character center)
            odd_start, odd_length = self._expand(s, current, current)
            # Check even-length palindrome (between two characters)
            even_start, even_length = self._expand(s, current, current + 1)

            if odd_length > max_length:
                start = odd_start
                max_length = odd_length

            if even_length > max_length:
                start = even_start
                max_length = even_length

        return s[start : start + max_length]

    def _expand(self, s: str, left: int, right: int) -> tuple[int, int]:
        """
        Expand around center and return (start_index, length)
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # After loop, left and right are one step beyond the palindrome
        return (left + 1, right - left - 1)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "babad",  # Expected: "bab" or "aba"
        "cbbd",  # Expected: "bb"
        "a",  # Expected: "a"
        "ac",  # Expected: "a" or "c"
        "racecar",  # Expected: "racecar"
        "abcdcda",  # Expected: "cdcdc" or "dcdc"
    ]

    for test in test_cases:
        result = solution.longestPalindrome(test)
        print(f"Input: '{test}' → Longest palindromic substring: '{result}'")
