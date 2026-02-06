class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp = [[0]*n for _ in range(m)]
        MOD = (10 ** 9) +7

        dp[startRow][startColumn] = 1

        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        ans = 0

        for step in range(1, maxMove+1):
            Next = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue
                    ways = dp[r][c] 
                    for dr ,dc in dirs:
                        if (r+dr) < 0 or (r+dr) >= m or (c+dc) < 0 or (c+dc) >= n:
                            ans = (ans+ways)% MOD
                        else:
                            Next[r+dr][c+dc] = (Next[r+dr][c+dc] + ways) % MOD
            dp = Next

        return ans