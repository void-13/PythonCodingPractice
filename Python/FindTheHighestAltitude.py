"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between
points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: O(n)
Space Complexity: O(1)
"""

def largestAltitude(gain):
    if not gain:
        return 0

    highest_altitude = 0
    current_sum = 0

    for alt in gain:
        current_sum += alt
        highest_altitude = max(highest_altitude, current_sum)

    return highest_altitude


# Test the function
if __name__ == "__main__":
    gain = [-4, -3, -2, -1, 4, 3, 2]
    print(largestAltitude(gain))
