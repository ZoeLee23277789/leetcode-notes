# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        count_p = False
        count_q = False

        def dfs (node):
            if not node:
                return None

            if node == p:
                return node
            if node== q:
                return node

            right = dfs(node.right)      
            left = dfs(node.left)

            if left and right:
                return node
            return left or right

        return dfs(root)
            