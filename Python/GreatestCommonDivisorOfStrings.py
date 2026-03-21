"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Time Complexity: O(m+n)
Space Complexity: O(m+n)
"""

import math


class GreatestCommonDivisorOfStrings:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[: math.gcd(len(str1), len(str2))]


if __name__ == "__main__":
    str1 = "AAAAAB"
    str2 = "AAA"
    print(GreatestCommonDivisorOfStrings().gcdOfStrings(str1, str2))
