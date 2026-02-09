class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 這題需要
        # 最大長度（max）
        # 達到最大長度的路徑數量（count）
        if len(nums) == 0:
            return 0

        length = [1] * len(nums)
        count = [1] * len(nums)
        ans = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        L = max(length)

        for i in range(len(nums)):
            if length[i] == L:
                ans += count[i]
        return ans
    


