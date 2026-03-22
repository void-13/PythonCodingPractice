def can_place_flowers(flowerbed, n):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not flowerbed:
        return False

    count = 0
    for i in range(len(flowerbed)):
        left_empty = (i == 0) or (flowerbed[i - 1] == 0)
        right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

        if left_empty and flowerbed[i] == 0 and right_empty:
            flowerbed[i] = 1
            count += 1

    return count >= n


flowerbed = [1, 0, 0, 0, 1]
n = 2
print(can_place_flowers(flowerbed, n))
