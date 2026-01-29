# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        L_H = self.getLeftHeight(root)
        # print("L_H = " , L_H)

        R_H = self.getRightHeight(root)
        # print("R_H = " , R_H)

        if L_H == R_H:  # 滿二元樹
            return (2**L_H)-1 
        
        else:           # 不滿二元樹，只好往下拆
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


    def getLeftHeight(self,node):
        Lh = 0
        while node != None:
            Lh += 1
            node = node.left
        return Lh
    def getRightHeight(self,node):
        Rh = 0
        while node != None:
            Rh += 1
            node = node.right
        return Rh

