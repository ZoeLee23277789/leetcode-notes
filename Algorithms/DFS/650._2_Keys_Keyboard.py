class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 0
        # 𝑑𝑝[𝑖] = 𝑚𝑖𝑛 (𝑗//𝑖) (𝑑𝑝[𝑖], 𝑑𝑝[𝑗] + 𝑖//𝑗, 𝑑𝑝[𝑖//𝑗] + 𝑗)
        dp = [float('inf')]*(n+1)
        dp[0] = 1

        for i in range(2, n+1):
            dp[i] = i
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i] , dp[j] + (i//j) , dp[i//j]+j) 

        return dp[n]
        
        # dp[i] => 做出剛好 i 個 'A' 所需要的最少操作次數
        # dp[j] + (i//j) => 先做到 j 個 A（花 dp[j] 步）+ Copy All（1 步）+ Paste (i//j - 1) 次
        # dp[i//j] + j => 先把 j 做出來，再用 Copy + Paste 把它放大到 i


        