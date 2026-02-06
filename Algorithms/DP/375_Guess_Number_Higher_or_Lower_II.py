class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 最壞成本是： x + max(左邊成本, 右邊成本)
        # minimax（極小化最大值）

        memo = {}

        def slove(start , end):
            if start >= end:
                return 0

            if (start,end) in memo:
                return memo[(start,end)]
            
            ans = float('Inf')

            for num in range(start,end+1):
                cost = num + max(slove(start,num-1),slove(num+1,end))
                ans = min(ans , cost)
            
            return ans
        return slove(0,n)


