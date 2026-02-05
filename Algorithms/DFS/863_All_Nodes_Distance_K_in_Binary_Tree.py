# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """

        # 答案其實只有三個方向：
        #     往左孩子
        #     往右孩子
        #     往爸爸（父節點） ← 這個最容易被忽略

        # 知道他們的根結點(parent), 把tree 變成無向圖
        parent = {}
        def dfs(node,par):
            if not node:
                return 
            parent[node] =  par

            dfs(node.left , node)
            dfs(node.right , node)
        dfs(root , None)
        # ===============================================================
        # Phase2 : BFS from target
        queue = deque( [(target , 0 )] )
        visited = set([target])
        ans = []
        # print("queue = " , queue)

        while queue:
            node ,distance = queue.popleft()
            # print("node = " , node)
            # print("distance = " , distance)

            if distance == k:
                ans.append(node.val)
                continue
            for neighbor in (node.left , node.right , parent[node]):
                if neighbor is not None and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance+1))
        return ans

            
            


            