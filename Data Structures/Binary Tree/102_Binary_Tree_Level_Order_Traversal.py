# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        q = deque([root])

        ans = []

        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left != None:
                    q.append(node.left)

                if node.right != None:
                    q.append(node.right)

            ans.append(level)
        return ans








# 102_Binary_Tree_Level_Order_Traversal