# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order. Return the shortest such subarray and output its length.
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        left = -1
        right = -1
        max_element = float("-inf")
        min_element = float("inf")

        # Pass 1: Left to Right - Find right boundary
        for i in range(n):
            max_element = max(nums[i], max_element)
            if nums[i] < max_element:
                right = i

        # Pass 2: Right to Left - Find left boundary
        for j in range(n - 1, -1, -1):
            min_element = min(nums[j], min_element)
            if nums[j] > min_element:
                left = j

        # If array is already sorted
        if right == -1:
            return 0

        return right - left + 1


# Test the solution
if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 6, 4, 8, 10, 9, 15]
    print(solution.findUnsortedSubarray(nums1))  # Output: 5

    nums2 = [1, 2, 3, 4]
    print(solution.findUnsortedSubarray(nums2))  # Output: 0

    nums3 = [1]
    print(solution.findUnsortedSubarray(nums3))  # Output: 0

    nums4 = [2, 3, 5, 4, 1, 6, 7]
    print(solution.findUnsortedSubarray(nums4))  # Output: 5
