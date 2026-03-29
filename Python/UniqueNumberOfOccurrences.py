"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def uniqueOccurrences(self, arr):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if arr is None:
            return False

        # Count frequencies using a dictionary
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Create a set of frequencies
        freq_set = set(freq_map.values())

        return len(freq_map) == len(freq_set)


# Test
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 2, 1, 1, 3]
    print(solution.uniqueOccurrences(arr))  # Output: True
