class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                # print(j)  
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)

            # print("------------------------")
        return max(dp)