class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        
        from collections import Counter
        
        # 1. 統計每個數值的總分
        count = Counter(nums)
        max_num = max(nums)
        
        points = [0] * (max_num + 1)
        for num in count:
            points[num] = num * count[num]
        
        # 2. DP（House Robber）
        dp = [0] * (max_num + 1)
        dp[0] = points[0]
        if max_num >= 1:
            dp[1] = max(points[0], points[1])
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
        
        return dp[max_num]
