"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import Counter


def max_operations(nums, k):
    # Single pass approach: check if complement exists before adding to map
    freq = Counter()
    count = 0

    for num in nums:
        diff = k - num
        # If complement already in map, pair them up
        if freq[diff] > 0:
            count += 1
            freq[diff] -= 1
        else:
            # No complement found, add current number to map
            freq[num] += 1

    return count


if __name__ == "__main__":
    print(max_operations([1, 2, 3, 4], 5))  # Output: 2
    print(max_operations([3, 1, 3, 4, 3], 6))  # Output: 1
    print(max_operations([3, 3, 3], 6))  # Output: 1
