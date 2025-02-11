# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        return root

# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)

#         currentNode = root

#         while True:
#             if val > currentNode.val:
#                 if not currentNode.right:
#                     currentNode.right = TreeNode(val)
#                 currentNode = currentNode.right
#             else:
#                 if not currentNode.left:
#                     currentNode.left = TreeNode(val)
#                 currentNode = currentNode.left