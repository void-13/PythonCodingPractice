"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        left = 0

        for right in range(len(t)):
            if left < len(s):
                s_char = s[left]
                t_char = t[right]

                if s_char == t_char:
                    left += 1

        return left == len(s)


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test 1
    s = "abc"
    t = "ahbgdc"
    result = solution.isSubsequence(s, t)
    print(result)  # True

    # Test 2
    s = "axc"
    t = "ahbgdc"
    result = solution.isSubsequence(s, t)
    print(result)  # False

    # Test 3 - Empty s
    s = ""
    t = "ahbgdc"
    result = solution.isSubsequence(s, t)
    print(result)  # True

    # Test 4 - No match
    s = "abc"
    t = ""
    result = solution.isSubsequence(s, t)
    print(result)  # False

    # Test 5 - All zeros
    s = "abc"
    t = "abc"
    result = solution.isSubsequence(s, t)
    print(result)  # True
