"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: O(n)
Space Complexity: O(1)
"""


def find_max_average(nums, k):
    # Compute sum of first window
    window_sum = sum(nums[:k])
    max_avg = window_sum / k

    # Slide the window: add right element, remove left element
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        max_avg = max(max_avg, window_sum / k)

    return max_avg


if __name__ == "__main__":
    print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # Output: 12.75
    print(find_max_average([5], 1))  # Output: 5.0
