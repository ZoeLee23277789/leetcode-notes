class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for _ in range(n)] for k in range(m)]
        print(dp)

        for N in range(n):
            dp[0][N] = 1
        for M in range(m):
            dp[M][0] = 1
        print(dp)
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]