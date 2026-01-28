# Given a string s, find the length of the longest substring without duplicate characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class LongestSubstringWithoutRepeatingCharacter:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(min(m,n)) where m is the size of the charset
        left = 0
        max_count = 0
        char_map = {}

        for right in range(len(s)):
            right_element = s[right]

            # 1st approach to move left pointer

            # If element already exists in the window, shrink from left
            # while right_element in char_map:
            #     left_element = s[left]
            #     del char_map[left_element]
            #     left += 1
            # char_map[right_element] = 1

            # 2nd approach - Move left pointer to the index next to the last occurrence of right_element

            if right_element in char_map:
                left = max(left, char_map[right_element] + 1)

            # Update character's latest position
            char_map[right_element] = right

            # Calculate max length
            substring_size = right - left + 1
            max_count = max(max_count, substring_size)

        return max_count


# Test cases
if __name__ == "__main__":
    lss = LongestSubstringWithoutRepeatingCharacter()
    print(lss.lengthOfLongestSubstring(""))  # Output: 0
    print(lss.lengthOfLongestSubstring("abbbb"))  # Output: 2
    print(lss.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(lss.lengthOfLongestSubstring("pwwkew"))  # Output: 3
    print(lss.lengthOfLongestSubstring("abba"))  # Output: 2
