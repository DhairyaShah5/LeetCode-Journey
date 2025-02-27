"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def cloneUsingDfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copyNode = Node(node.val)
            oldToNew[node] = copyNode

            for neighbor in node.neighbors:
                copyNode.neighbors.append(cloneUsingDfs(neighbor))
            return copyNode

        return cloneUsingDfs(node) if node else None