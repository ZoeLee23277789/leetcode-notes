class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        Index1 = -1
        Index2 = -1
        ans = float("inf")

        for i, w in enumerate(wordsDict):
            if w == word1:
                Index1 = i
                if Index2 != -1:
                    ans = min(ans, abs(Index1 - Index2))
            if w == word2:
                Index2 = i
                if Index1 != -1:
                    ans = min(ans, abs(Index1 - Index2))
        return ans


        