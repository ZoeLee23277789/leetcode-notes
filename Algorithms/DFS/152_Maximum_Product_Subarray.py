class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = Max = Min = nums[0]

        for num in nums[1:]:
            prev_max = Max
            prev_min = Min

            Max = max(num, prev_max*num, prev_min*num)
            Min = min(num, prev_max*num, prev_min*num)

            ans = max(ans, prev_max, prev_min)

        return ans
