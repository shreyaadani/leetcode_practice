# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        def func(root,res):
            if root is not None:
                func(root.left,res)
                res.append(root.val)
                func(root.right,res)
        res = []
        func(root,res)
        return res
        
        