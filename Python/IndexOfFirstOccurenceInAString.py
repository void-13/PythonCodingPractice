"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=two-pointers
"""


class Solution:
    """
    Time Complexity: O(n*m)
    Space Complexity: O(1)
    """

    def strStr(self, haystack: str, needle: str) -> int:
        haystack_index = 0
        haystack_length = len(haystack)
        needle_length = len(needle)

        while haystack_index < haystack_length:
            start = haystack_index
            needle_index = 0

            while (
                haystack_index < haystack_length
                and needle_index < needle_length
                and haystack[haystack_index] == needle[needle_index]
            ):
                haystack_index += 1
                needle_index += 1

            if needle_index == needle_length:
                return start

            haystack_index = start + 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    haystack = "leetcode"
    needle = "code"

    result = solution.strStr(haystack, needle)
    print(result)
