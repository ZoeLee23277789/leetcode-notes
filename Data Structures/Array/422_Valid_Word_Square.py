class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        num = len(words)
        for i in range(len(words)):
            # print("i=" , i)
            for j in range(len(words[i])):
                if j >= num or i >= len(words[j]):
                    return False

                if words[i][j] != words[j][i]:
                    return False
        return True