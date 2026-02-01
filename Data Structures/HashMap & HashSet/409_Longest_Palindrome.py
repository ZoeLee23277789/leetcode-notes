class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        count = 0
        flag = 0

        # 存成dic 的資料結構
        for i in s :
            dic[i] = dic.get(i , 0) +1

        # 計算是成對 (palindrome)

        for val in dic.values():
            count += (val//2)*2

            if (val % 2) == 1:
                flag = 1
        return count + flag
        









