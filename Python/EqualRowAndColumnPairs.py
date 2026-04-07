"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

Time Complexity: O(n²)
Space Complexity: O(n²)
"""

from collections import Counter


def equal_pairs(grid):
    if not grid:
        return 0

    row_count = Counter(tuple(row) for row in grid)

    count = 0
    for col in range(len(grid)):
        column = tuple(grid[row][col] for row in range(len(grid)))
        count += row_count.get(column, 0)

    return count


if __name__ == "__main__":
    grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    print(equal_pairs(grid))
