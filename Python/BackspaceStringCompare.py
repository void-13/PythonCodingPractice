#     Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character. Note that after backspacing an empty text, the text will continue empty.
#     https://leetcode.com/problems/backspace-string-compare/description/
class Solution:
    # time complexity: O(n + m)
    # space complexity: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            i = self.get_next_valid(s, i)
            j = self.get_next_valid(t, j)

            if (i >= 0) != (j >= 0):
                return False

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True

    def get_next_valid(self, string: str, index: int) -> int:
        skip = 0

        while index >= 0:
            if string[index] == "#":
                skip += 1
                index -= 1
            elif skip > 0:
                skip -= 1
                index -= 1
            else:
                break

        return index
