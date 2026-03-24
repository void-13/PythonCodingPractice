"""
Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[left] != 0 and nums[right] != 0:
                left += 1
            elif nums[left] == 0 and nums[right] != 0:
                # Swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test 1
    input1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(input1)
    print(input1)  # [1, 3, 12, 0, 0]

    # Test 2
    input2 = [0]
    solution.moveZeroes(input2)
    print(input2)  # [0]

    # Test 3
    input3 = []
    solution.moveZeroes(input3)
    print(input3)  # []

    # Test 4
    input4 = [1, 2, 3, 4, 5]
    solution.moveZeroes(input4)
    print(input4)  # [1, 2, 3, 4, 5]

    # Test 5
    input5 = [0, 0, 0, 0]
    solution.moveZeroes(input5)
    print(input5)  # [0, 0, 0, 0]

    # Test 6
    input6 = [0, 1, 0, 2, 0, 3]
    solution.moveZeroes(input6)
    print(input6)  # [1, 2, 3, 0, 0, 0]
