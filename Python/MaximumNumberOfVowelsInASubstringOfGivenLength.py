"""
Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not s or len(s) < k:
            return 0

        vowels = "aeiouAEIOU"
        count = 0

        # Count vowels in first window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        vowel_count = count
        left = 0

        # Slide the window
        for right in range(k, len(s)):
            # Remove left character if vowel
            if s[left] in vowels:
                count -= 1

            # Add right character if vowel
            if s[right] in vowels:
                count += 1

            left += 1
            vowel_count = max(count, vowel_count)

        return vowel_count


if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    k = 3
    print(solution.maxVowels(s, k))  # Output: 2
