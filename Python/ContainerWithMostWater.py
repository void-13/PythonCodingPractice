# You are given an integer array height of length n. There are n vertical lines drawn
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Time Complexity: O(n)
# Space Complexity: O(1)


def max_area(containerHeight):
    # edge case: empty or single element
    if len(containerHeight) == 0 or len(containerHeight) == 1:
        return 0

    maxArea = 0
    left = 0
    right = len(containerHeight) - 1

    while left < right:
        # calculate current area
        area = min(containerHeight[left], containerHeight[right]) * (right - left)

        # update max area
        maxArea = max(area, maxArea)

        # move the pointer with smaller height
        if containerHeight[left] < containerHeight[right]:
            left += 1
        else:
            right -= 1

    return maxArea


# main
height = [1, 3, 2, 5, 25, 24, 5]
print(max_area(height))  # 24
