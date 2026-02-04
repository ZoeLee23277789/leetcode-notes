class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        currSum = 0
        ans = nums[0]

        for right in range(len(nums)):
            currSum += nums[right]
            ans = max(ans,currSum)

            if currSum < 0:
                currSum = 0
                left = right + 1

        return ans   
