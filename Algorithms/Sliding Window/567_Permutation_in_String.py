class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        # 1) 統計 s1
        dic1 = {}
        for ch in s1:
            dic1[ch] = dic1.get(ch, 0) + 1

        # 2) 初始化第一個 window（長度 = len(s1)）
        left = 0
        right = len(s1)  # right 是「右界」，不包含
        dic2 = {}
        for ch in s2[left:right]:
            dic2[ch] = dic2.get(ch, 0) + 1

        # 3) 開始滑動：每次比較，再更新 window
        while True:
            if dic2 == dic1:
                return True

            if right == len(s2):  # 不能再往右滑了
                break

            # 加進右邊新字母
            add_ch = s2[right]
            dic2[add_ch] = dic2.get(add_ch, 0) + 1

            # 移除左邊舊字母
            remove_ch = s2[left]
            dic2[remove_ch] -= 1
            if dic2[remove_ch] == 0:
                del dic2[remove_ch]

            left += 1
            right += 1

        return False
