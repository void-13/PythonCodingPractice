from typing import List

"""
Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.
https://leetcode.com/problems/next-permutation/description/?envType=problem-list-v2&envId=two-pointers
"""


class NextPermutation:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def nextPermutation(self, nums: List[int]) -> None:
        nums_length = len(nums)
        index = -1

        if nums_length == 0 or nums_length == 1:
            return

        # Step 1: Find pivot (scan right to left, find first element smaller than its right neighbor)
        right = nums_length - 1
        while right > 0:
            if nums[right] <= nums[right - 1]:
                right -= 1
            else:
                index = right - 1
                break

        # Step 2: If no pivot found, reverse entire array
        if index == -1:
            left, r = 0, nums_length - 1
            while left < r:
                nums[left], nums[r] = nums[r], nums[left]
                left += 1
                r -= 1
            return

        # Step 3: Find swap candidate (scan right to left, find first element greater than pivot)
        for i in range(nums_length - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break

        # Step 4: Reverse the suffix after pivot index
        left, r = index + 1, nums_length - 1
        while left < r:
            nums[left], nums[r] = nums[r], nums[left]
            left += 1
            r -= 1


if __name__ == "__main__":
    obj = NextPermutation()

    input1 = [1, 2, 3]
    obj.nextPermutation(input1)
    print(f"Input: [1,2,3] -> Output: {input1}")

    input2 = [3, 2, 1]
    obj.nextPermutation(input2)
    print(f"Input: [3,2,1] -> Output: {input2}")

    input3 = [4, 5, 9, 8, 7, 6]
    obj.nextPermutation(input3)
    print(f"Input: [4,5,9,8,7,6] -> Output: {input3}")

    input4 = [1, 1, 5]
    obj.nextPermutation(input4)
    print(f"Input: [1,1,5] -> Output: {input4}")

    input5 = [8, 7, 9, 1]
    obj.nextPermutation(input5)
    print(f"Input: [8,7,9,1] -> Output: {input5}")

    input6 = [8, 6, 4, 1]
    obj.nextPermutation(input6)
    print(f"Input: [8,6,4,1] -> Output: {input6}")
