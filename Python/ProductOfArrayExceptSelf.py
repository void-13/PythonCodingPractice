def product_except_self(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums or len(nums) <= 1:
        return nums

    answer = [1] * len(nums)

    for i in range(1, len(nums)):
        answer[i] = answer[i - 1] * nums[i - 1]

    right_product = 1
    for j in range(len(nums) - 1, -1, -1):
        answer[j] *= right_product
        right_product *= nums[j]

    return answer


nums = [1, 2, 3, 4]
print(product_except_self(nums))
