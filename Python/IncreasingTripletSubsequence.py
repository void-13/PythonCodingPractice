def increasing_triplet(nums: list[int]) -> bool:
    if not nums or len(nums) < 3:
        return False

    first = float("inf")
    second = float("inf")

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False


if __name__ == "__main__":
    nums = [2, 1, 5, 0, 4, 6]
    print(increasing_triplet(nums))
