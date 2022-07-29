# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = []
        def minDepthF(root, x):
            if root:
                minDepthF(root.left, x+1)
                if not root.left and not root.right:
                    stack.append(x)
                minDepthF(root.right, x+1)
        
        minDepthF(root, 1)
        
        return min(stack)
        