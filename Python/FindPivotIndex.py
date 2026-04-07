class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        if not nums:
            return -1

        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Right sum = total - left - current element
            right_sum = total_sum - left_sum - num

            if left_sum == right_sum:
                return i

            left_sum += num

        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()

    print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
    print(solution.pivotIndex([1, 2, 3]))            # Output: -1
    print(solution.pivotIndex([2, 1, -1]))           # Output: 0
