class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = set(nums)
        ans = []
        
        for i in range(1,len(nums)+1):
            if i not in num:
                ans.append(i)
        return ans
        