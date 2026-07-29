# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def dfs(node):
            if node is None:
                return 0

            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)
            self.maxDiameter = max(self.maxDiameter, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)

        dfs(root)

        return self.maxDiameter