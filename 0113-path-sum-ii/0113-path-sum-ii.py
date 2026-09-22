# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        pathlists = []
        self.dfs(root,targetSum,[],pathlists)
        return pathlists


    def dfs(self,node:TreeNode,remainingsum:int,pathnodes:List[int],pathlists:List[List[int]]):
        if not node:
            return

        pathnodes.append(node.val)

        if remainingsum == node.val and not node.left and not node.right:
            pathlists.append(list(pathnodes))
        else:
            self.dfs(node.left,remainingsum-node.val,pathnodes,pathlists)  
            self.dfs(node.right,remainingsum-node.val,pathnodes,pathlists)         
        pathnodes.pop()



        