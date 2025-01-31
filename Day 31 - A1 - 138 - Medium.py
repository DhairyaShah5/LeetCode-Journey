"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        originalToCopy = {None: None}
        current = head

        while current:
            copyNode = Node(current.val)
            originalToCopy[current] = copyNode
            current = current.next
        
        current = head
        while current:
            copyNode = originalToCopy[current]
            copyNode.next = originalToCopy[current.next]
            copyNode.random = originalToCopy[current.random]
            current = current.next

        return originalToCopy[head]