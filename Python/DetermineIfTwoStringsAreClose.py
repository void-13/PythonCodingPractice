from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # If lengths are different, they can never be close
        if len(word1) != len(word2):
            return False

        # Count frequencies of each character
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        # Check 1: Both strings must contain the exact same set of unique characters
        # This satisfies Operation 2's requirement that characters must exist to be swapped
        if set(cnt1.keys()) != set(cnt2.keys()):
            return False

        # Check 2: The sorted frequencies must be identical
        # Operation 2 allows us to reassign frequencies to different characters,
        # so as long as the "pattern" of counts is the same, we can transform them.
        return sorted(cnt1.values()) == sorted(cnt2.values())


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.closeStrings("cabbba", "abbccc"))  # Output: True
