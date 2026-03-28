"""
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
"""


class LongestSubarrayOf1sAfterDeletingOneElement:
    def longest_subarray(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if nums is None or len(nums) == 0:
            return 0

        zero_count = 0
        max_length = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length


if __name__ == "__main__":
    solution = LongestSubarrayOf1sAfterDeletingOneElement()

    # Test cases
    print(solution.longest_subarray([1, 1, 1, 1]))  # 3
    print(solution.longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
    print(solution.longest_subarray([1, 1, 0, 1]))  # 3
    print(solution.longest_subarray([1, 1, 1]))  # 2
    print(solution.longest_subarray([0, 0, 0]))  # 0
