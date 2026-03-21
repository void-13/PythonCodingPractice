"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end
of the merged string. Return the merged string.

Time Complexity: O(m+n)
Space Complexity: O(m+n)
"""


class MergeStringsAlternately:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 or not word2:
            return ""

        result = []
        counter = 0

        while counter < len(word1) and counter < len(word2):
            result.append(word1[counter])
            result.append(word2[counter])
            counter += 1

        while counter < len(word1):
            result.append(word1[counter])
            counter += 1

        while counter < len(word2):
            result.append(word2[counter])
            counter += 1

        return "".join(result)


if __name__ == "__main__":
    word1 = "ab"
    print("word1:", word1)
    word2 = "pqrst"
    print("word2:", word2)
    m = MergeStringsAlternately()
    result = m.mergeAlternately(word1, word2)
    print("result:", result)
