# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        troot = []
        tsub = []
        def dfs(node, stack):
            if not node:
                return
            stack.append(node.val)
            dfs(node.left, stack)
            
            dfs(node.right, stack)
            
            
        dfs(root, troot)
        dfs(subRoot, tsub)

        return any(troot[i:i+len(tsub)] == tsub for i in range(len(troot) - len(tsub) + 1))