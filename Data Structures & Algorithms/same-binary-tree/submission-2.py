# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node0, node1):
            if not node0 and not node1:
                return True
            if not node0 or not node1:
                return False
            if node0.val != node1.val:
                return False
            return dfs(node0.left, node1.left) and dfs(node0.right, node1.right)
        
        res = dfs(p, q)

        return res