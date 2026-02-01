# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        low = 0
        max_length = 0
        zero_count = 0

        for high in range(len(nums)):
            if nums[high] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[low] == 0:
                    zero_count -= 1
                low += 1

            max_length = max(max_length, high - low + 1)

        return max_length


# Test
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    print(solution.longestOnes(nums, k))  # Expected: 6
