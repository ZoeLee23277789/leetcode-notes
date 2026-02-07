class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [[2]*len(arr) for _ in range(len(arr))]
        # print(dp)
        ans = 0
        idx_map = {}
        for idx,val in enumerate(arr):
            idx_map[val] = idx
        # print(idx_map)
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                # 如果存在 k 使得 arr[i] + arr[j] = arr[k]
                    # 就可以把序列延長成：... , arr[i], arr[j], arr[k]
                    # 所以 dp[j][k] = dp[i][j] + 1
                if arr[i]+arr[j] in idx_map: # xi + xi+1 == xi+2
                    k = idx_map[arr[i]+arr[j]]
                    dp[j][k] = max(dp[j][k],dp[i][j]+1)
                    ans = max(ans , dp[j][k])

        if ans >= 3:
            return ans
        else:
            return 0
