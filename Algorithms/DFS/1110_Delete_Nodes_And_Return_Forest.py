# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        delete_set = set(to_delete)
        ans = []
        def dfs (node , is_root):
            if not node:
                return
            deleted = node.val in delete_set
            # 如果目前這個 node 是一棵樹的根，而且它不會被刪 → 加入答案
            if is_root and not deleted:
                ans.append(node)
                
            node.left = dfs(node.left , deleted)
            node.right = dfs(node.right, deleted)

            if deleted:
                return None
            else:
                return node
        dfs(root,True)
        return ans





        