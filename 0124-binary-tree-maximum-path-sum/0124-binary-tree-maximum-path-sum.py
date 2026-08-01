# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = root.val
        self.dfs(root)

        return self.res

    def dfs(self,node):
            if not node:
                return 0

            if not node.left and not node.right:
                self.res = max(self.res,node.val)
                return node.val
            
            left = self.dfs(node.left)
            right = self.dfs(node.right)

            self.res = max(self.res, node.val , node.val+ left , node.val + right , node.val+ right + left)

            return max(0,node.val, node.val + left , node.val + right)


        