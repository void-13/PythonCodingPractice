def reverse_array(arr, m):
    # Edge case check
    if m < 0 or m >= len(arr) - 1:
        return

    left = m + 1
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1