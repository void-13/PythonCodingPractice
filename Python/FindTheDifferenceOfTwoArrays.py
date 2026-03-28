"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
"""


class FindTheDifferenceOfTwoArrays:
    def find_difference(self, nums1, nums2):
        """
        Time Complexity: O(n + m) where n = len(nums1), m = len(nums2)
        Space Complexity: O(n + m)
        """
        nums1_set = set(nums1)  # O(n)
        nums2_set = set(nums2)  # O(m)

        nums1_list = []  # O(n)
        nums2_list = []  # O(m)

        for num in nums1_set:  # O(n)
            if num not in nums2_set:
                nums1_list.append(num)

        for num in nums2_set:  # O(m)
            if num not in nums1_set:
                nums2_list.append(num)

        return [nums1_list, nums2_list]


if __name__ == "__main__":
    solution = FindTheDifferenceOfTwoArrays()

    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    print(solution.find_difference(nums1, nums2))  # [[3], []]

    nums3 = [1, 2, 3]
    nums4 = [2, 4, 6]
    print(solution.find_difference(nums3, nums4))  # [[1, 3], [4, 6]]
