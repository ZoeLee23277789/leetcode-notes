class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[float('Inf')]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        # print(dp)
        dp[1][1] = grid[0][0]

        for i in range(1, len(grid)+1):
            for j in range(1, len(grid[0])+1):
                if i == 1 and j == 1:
                    continue

                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]

        return dp[len(grid)][len(grid[0])]

        