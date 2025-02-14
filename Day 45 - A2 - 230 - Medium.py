# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
# Property: Inorder traversal of a Binary Search Tree always gives nodes in sorted order.
        result = []

        def inorderTraversal(node):
            if not node:
                return 

            inorderTraversal(node.left)
            result.append(node.val)
            inorderTraversal(node.right)
        
        inorderTraversal(root)

        return result[k-1]