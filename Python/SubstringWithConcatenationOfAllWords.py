"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of
any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/?envType=problem-list-v2&envId=sliding-window
"""

from typing import List


class SubstringWithConcatenationOfAllWords:
    """
    Time Complexity: O(m*n) where m is the length of the string and n is the length of each word
    Space Complexity: O(n) where n is the number of words
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []

        # edge case check
        if not s or not words:
            return result

        str_len = len(s)
        word_len = len(words[0])
        total_words = len(words)

        # build frequency map of all words
        total_word_frequency = {}
        for word in words:
            total_word_frequency[word] = total_word_frequency.get(word, 0) + 1

        # slide window starting at each offset from 0 to word_len
        for start in range(word_len):
            window_frequency = {}  # frequency map for current window
            left = start
            right = start
            count = 0  # number of valid words in current window

            while right + word_len <= str_len:
                # extract next word from right pointer
                substring = s[right: right + word_len]
                right += word_len

                if substring in total_word_frequency:
                    # add word to window frequency
                    window_frequency[substring] = window_frequency.get(substring, 0) + 1
                    count += 1

                    # if word is overused, shrink window from left until valid
                    while window_frequency[substring] > total_word_frequency[substring]:
                        left_word = s[left: left + word_len]
                        window_frequency[left_word] -= 1
                        count -= 1
                        left += word_len

                    # all words matched, record starting index
                    if count == total_words:
                        result.append(left)
                        # shrink window from left to continue searching
                        left_word = s[left: left + word_len]
                        window_frequency[left_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    # invalid word found, reset window completely
                    window_frequency.clear()
                    count = 0
                    left = right

        return result


# Test
sol = SubstringWithConcatenationOfAllWords()
print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))                  # [0, 9]
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))  # []
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))       # [6, 9, 12]