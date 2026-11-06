# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parent = {root:None}
        queue = deque([root])

        while queue and (p not in parent or q not in parent):
            node = queue.popleft()

            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            
            if node.right:
                parent[node.right] = node
                queue.append(node.right)\

        ancestors = set()

        curr= p
        while curr is not None:
            ancestors.add(curr)
            curr = parent[curr]

        curr = q
        while curr not in ancestors:
            curr = parent[curr]


        return curr    




        