# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


class Solution:
    def minPathSum(self, grid):

        numrows = len(grid)  # number of rows
        numcols = len(grid[0])  # number of columns

        for i in range(1, numrows):  # does first row
            grid[0][i] += grid[0][i - 1]
            print(grid)

        # Original input
        # [
        #   [1,3,1],
        #   [1,5,1],
        #   [4,2,1]
        # ]
        # first pass
        # [
        #   [1,4,1],
        #   [1,5,1],
        #   [4,2,1]
        # ]
        # second pass
        # [
        #   [1,4,5],
        #   [1,5,1],
        #   [4,2,1]
        # ]

        for i in range(1, numcols):  # does first column
            grid[i][0] += grid[i - 1][0]
            print(grid)

        # Original input
        # [
        #   [1,3,1],
        #   [1,5,1],
        #   [4,2,1]
        # ]
        # first pass
        # [
        #   [1,3,1],
        #   [2,5,1],
        #   [4,2,1]
        # ]
        # second pass
        # [
        #   [1,3,1],
        #   [2,5,1],
        #   [4,2,1]
        # ]

        for i in range(1, numrows):  # does the rest
            for j in range(1, numcols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                print(grid)

        # grid looks like this by the time it gets there
        # [
        #   [1,4,5],
        #   [2,5,1],
        #   [4,2,1]
        # ]
        # first pass of i loop, first pass of j loop
        # [
        #   [1,4,5],
        #   [2,7,1],
        #   [4,2,1]
        # ]
        # first pass of i loop, second pass of j loop
        # [
        #   [1,4,5],
        #   [2,7,1],
        #   [4,6,1]
        # ]
        # second pass of i loop, first pass of j loop
        # [
        #   [1,4,5],
        #   [2,7,6],
        #   [4,6,1]
        # ]
        # second pass of i loop, second pass of j loop
        # [
        #   [1,4,5],
        #   [2,7,6],
        #   [4,6,7]
        # ]

        return grid[-1][-1]


x = Solution()
print(x.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
