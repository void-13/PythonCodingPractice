# Given an array nums of n integers, return an array of all the unique quadruplets...
# https://leetcode.com/problems/4sum/description/
class Solution:

    # Time Complexity: O(n^3)
    # Space Complexity: O(1)
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []

        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
