class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # window 裡面「不是最多的那個字母」都要被改

        freq = {}
        l = 0    # length
        max_freq = 0
        best = 0

        for r in range(len(s)):
            ch = s[r]
            # print("ch = " , ch)
            freq[ch] = freq.get(ch, 0) + 1
            # print("freq = " , freq)
            max_freq = max(max_freq, freq[ch]) # 找到最大freq的字

            # 不合法：需要替換的次數 > k
            while (r - l + 1) - max_freq > k:   #需要改的次數 = window 長度 - 最多字母的次數
                freq[s[l]] -= 1
                l += 1

            best = max(best, r - l + 1)

        return best


        