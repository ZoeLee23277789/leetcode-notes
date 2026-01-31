class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        arr = sorted(s,reverse = True)

        if len(arr) >= 3:
            return arr[2]

        return arr[0]