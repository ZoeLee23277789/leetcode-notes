# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def sameTree(node , subnode):
            if not node and not subnode:
                return True
            if not node or not subnode:
                return False
            if node.val != subnode.val:
                return False
            return sameTree(node.left,subnode.left) and sameTree(node.right, subnode.right)
        
        if not subRoot:
            return True
        
        if not root:
            return False

        if sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.right , subRoot) or self.isSubtree(root.left , subRoot) 

        

        