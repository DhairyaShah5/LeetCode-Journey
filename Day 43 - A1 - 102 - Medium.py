# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            level = []

            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if level:
                result.append(level)
                
        return result
        
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         result = []

#         def dfs(node, depth):
#             if not node:
#                 return None
#             if len(result) == depth:
#                 result.append([])

#             result[depth].append(node.val)
#             dfs(node.left, depth + 1)
#             dfs(node.right, depth + 1)

#         dfs(root, 0)
#         return result