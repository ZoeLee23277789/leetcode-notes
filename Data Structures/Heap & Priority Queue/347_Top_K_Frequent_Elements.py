class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}
        ans = []
        for i in nums:
            dic[i] = dic.get(i , 0) +1

        items = sorted(dic.items() , key = lambda x: x[1] , reverse=True) 

        for j in range(k):
            ans.append(items[j][0])
        return ans