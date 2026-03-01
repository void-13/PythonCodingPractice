"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=two-pointers
"""


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0  # slow pointer - tracks where to place next valid element

        for i in range(len(nums)):  # fast pointer - scans every element
            if nums[i] != val:
                nums[count] = nums[i]  # place valid element at count position
                count += 1

        return count


# Test
sol = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
result = sol.removeElement(nums, val)
print(result)  # Output: 5
